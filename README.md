# HACK SOLO

## Overview

HACK SOLO Lab is a beginner-friendly web application security training platform developed for cybersecurity students. The project provides intentionally vulnerable labs that help learners understand common web application security issues in a safe and controlled environment.

This project is designed for educational purposes and can be deployed locally or within a private lab environment.

---

## Features

### Available Labs

* SQL Injection (SQLi)
* Cross-Site Scripting (XSS)
* File Upload Vulnerability
* Insecure Direct Object Reference (IDOR)
* Cross-Site Request Forgery (CSRF)
* Command Injection


### Dashboard

* Beginner-friendly interface
* Hacking-themed UI
* Easy navigation between labs
* Educational explanations

---

## Technologies Used

### Backend

* Python
* Flask

### Frontend

* HTML5
* CSS3
* Bootstrap

### Database

* MySQL / MariaDB

### Deployment

* Localhost
* Virtual Machines
* Docker (Optional)
* Cloud VPS (Optional)

---

## Project Structure

```text
SOLO/

├── app.py
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   ├── login.html
│   ├── xss_lab.html
│   ├── upload_lab.html
│   ├── csrf_lab.html
│   └── profile.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── uploads/
```

---

## Installation

### Clone Repository

```bash
https://github.com/neerajrajeev-in/HACK-SOLO.git
cd HACK-SOLO
```

### Create Virtual Environment

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### Install Dependencies

```bash
pip install flask flask-mysqldb
```

### Run Application

```bash
python3 app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

---

## Learning Objectives

Students can learn:

* OWASP Top 10 vulnerabilities
* Web application security fundamentals
* Secure coding practices
* Vulnerability identification
* Vulnerability remediation

---

## Educational Disclaimer

This project contains intentionally vulnerable code for cybersecurity education and awareness.

The project must only be used:

* On localhost
* Inside virtual machines
* Inside Docker containers
* In authorized lab environments

Do not use these techniques against systems without permission.

---

## Future Improvements

* Scoreboard System
* Student Progress Tracking
* API Security Labs
* JWT Authentication Labs
* Dockerized Challenges
* CTF Mode
* Admin Challenge Builder

---

## Author

HACK SOLO

Cybersecurity Student Project

Built for educational and training purposes.
****
