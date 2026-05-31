from flask import Flask, render_template, request
import os
import subprocess

app =  Flask(__name__)
# Banner
print(r"""
██╗  ██╗ █████╗  ██████╗██╗  ██╗
██║  ██║██╔══██╗██╔════╝██║ ██╔╝
███████║███████║██║     █████╔╝
██╔══██║██╔══██║██║     ██╔═██╗
██║  ██║██║  ██║╚██████╗██║  ██╗
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝

███████╗ ██████╗ ██╗      ██████╗
██╔════╝██╔═══██╗██║     ██╔═══██╗
███████╗██║   ██║██║     ██║   ██║
╚════██║██║   ██║██║     ██║   ██║
███████║╚██████╔╝███████╗╚██████╔╝
╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝
=========================================
[✓] SQL Injection Lab
[✓] XSS Lab
[✓] File Upload Lab
[✓] CSRF Lab
[✓] Command Injection Lab
[✓] IDOR LAB
=========================================
          HACK SOLO LAB
      Cyber Security Training Lab
=========================================
""")

# =========================
# APP CONFIG
# =========================
APP_NAME = "HACK SOLO LAB"

# =========================
# UPLOAD CONFIG
# =========================
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# =========================
# SAMPLE USERS
# =========================
users = {
    1: {"name": "Alice", "email": "alice@solo.lab"},
    2: {"name": "Bob", "email": "bob@solo.lab"},
    3: {"name": "Charlie", "email": "charlie@solo.lab"}
}

# =========================
# CSRF LAB EMAIL
# =========================
current_email = "student@solo.lab"

@app.route('/change-email', methods=['GET', 'POST'])
def change_email():
    global current_email

    if request.method == 'POST':
        current_email = request.form.get('email', current_email)

    return render_template(
        "csrf_lab.html",
        email=current_email,
        app_name=APP_NAME
    )

# =========================
# HOME PAGE
# =========================
@app.route('/')
def home():
    return render_template("index.html", app_name=APP_NAME)

# =========================
# DASHBOARD
# =========================
@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html", app_name=APP_NAME)

# =========================
# LOGIN
# =========================
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == "admin" and password == "admin":
            return "🔥 Login Success - HACK SOLO LAB"
        return "❌ Invalid Credentials"

    return render_template('login.html', app_name=APP_NAME)

# =========================
# SQLi LAB
# =========================
@app.route('/sqli', methods=['GET', 'POST'])
def sqli():
    message = ""

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == "admin" and password == "admin":
            message = "🔥 SQLi LAB: Login Successful (Admin)"
        else:
            message = "❌ Invalid Credentials"

    return render_template("sqli.html", message=message, app_name=APP_NAME)

# =========================
# XSS LAB
# =========================
@app.route('/xss', methods=['GET', 'POST'])
def xss():
    name = ""

    if request.method == 'POST':
        name = request.form['name']

    return render_template('xss_lab.html', name=name, app_name=APP_NAME)

# =========================
# FILE UPLOAD LAB (UPDATED)
# =========================
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    message = ""

    if request.method == 'POST':

        # safer request handling
        if 'file' not in request.files:
            message = "No file selected"
        else:
            file = request.files['file']

            if file.filename == "":
                message = "Please choose a file"
            else:
                filepath = os.path.join(
                    app.config['UPLOAD_FOLDER'],
                    file.filename
                )
                file.save(filepath)
                message = f"Uploaded: {file.filename}"

    return render_template(
        "upload_lab.html",
        message=message,
        app_name=APP_NAME
    )

# =========================
# CMD LAB (SAFE)
# =========================
@app.route('/cmd', methods=['GET', 'POST'])
def cmd():
    output = ""

    if request.method == 'POST':
        host = request.form.get('host', '').strip()

        if host:
            try:
                result = subprocess.run(
                    ["ping", "-c", "1", host],
                    capture_output=True,
                    text=True
                )
                output = result.stdout + result.stderr
            except Exception as e:
                output = str(e)
        else:
            output = "❌ No host provided"

    return render_template("cmd_lab.html", output=output, app_name=APP_NAME)

# =========================
# USER PROFILE
# =========================
@app.route("/user/<int:user_id>")
def user_profile(user_id):
    user = users.get(user_id)

    if not user:
        return "User Not Found"

    return render_template(
        "profile.html",
        user=user,
        user_id=user_id,
        app_name=APP_NAME
    )

# =========================
# RUN SERVER
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True,use_reloader=False )
