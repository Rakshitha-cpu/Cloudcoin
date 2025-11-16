from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = "cloudcoin-secret-key"

# Render base directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, "cloudcoin.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Upload folder (Render custom env variable will override this later)
app.config['UPLOAD_FOLDER'] = os.path.join(basedir, "uploads")
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5 MB limit

db = SQLAlchemy(app)

# -----------------------------------------------------
# USER MODEL
# -----------------------------------------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    coins = db.Column(db.Integer, default=0)
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# -----------------------------------------------------
# WORK SUBMISSION MODEL
# -----------------------------------------------------
class WorkSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    filename = db.Column(db.String(200))
    status = db.Column(db.String(20), default="Pending")


# -----------------------------------------------------
# ROUTES
# -----------------------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        if User.query.filter_by(email=email).first():
            flash("Email is already registered", "danger")
            return redirect(url_for("register"))

        user = User(name=name, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        flash("Registration successful! Please login.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            session["user_id"] = user.id
            session["user_name"] = user.name

            flash("Login successful!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid email or password", "danger")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        flash("Please login first!", "warning")
        return redirect(url_for("login"))

    user = User.query.get(session["user_id"])
    return render_template("dashboard.html", name=user.name, coins=user.coins)


@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully!", "info")
    return redirect(url_for("home"))


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if "user_id" not in session:
        flash("Please login first!", "warning")
        return redirect(url_for("login"))

    if request.method == "POST":
        file = request.files["file"]
        if file.filename == "":
            flash("No file selected!", "danger")
            return redirect(url_for("upload"))

        filename = secure_filename(file.filename)
        save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(save_path)

        submission = WorkSubmission(
            user_id=session["user_id"],
            filename=filename
        )
        db.session.add(submission)
        db.session.commit()

        flash("Work uploaded successfully!", "success")
        return redirect(url_for("dashboard"))

    return render_template("upload.html")


@app.route("/admin")
def admin():
    if "user_id" not in session:
        flash("Please login!", "warning")
        return redirect(url_for("login"))

    user = User.query.get(session["user_id"])
    if not user.is_admin:
        flash("Access denied!", "danger")
        return redirect(url_for("dashboard"))

    works = WorkSubmission.query.all()
    users = User.query.all()
    return render_template("admin.html", works=works, users=users)


# -----------------------------------------------------
# MAIN
# -----------------------------------------------------
if __name__ == "__main__":
    if not os.path.exists(app.config["UPLOAD_FOLDER"]):
        os.makedirs(app.config["UPLOAD_FOLDER"])

    with app.app_context():
        db.create_all()

    app.run(debug=True)
