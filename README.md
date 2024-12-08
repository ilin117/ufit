**UFIT: Fitness & Wellness Platform for College Students**
Welcome to UFIT, a web-based platform designed to help college students maintain a balanced and healthy lifestyle through personal trainer interaction, peer support, and access to wellness resources.

**Table of Contents**
Project Overview
Features
Tech Stack
Installation
Project Structure
Key Functionalities
Screenshots
Future Improvements
License
Project Overview
UFIT connects college students with personal trainers, wellness organizations, and peer workout groups at their campus. The platform supports setting connecting with fitness communities through posts, events, and global messaging.

**Features**
User Roles
Student: Access fitness events, personal trainers, and wellness programs.
Trainer: Create personalized workout programs and offer coaching.
Wellness Organization: Promote campus events and health services.
Core Functionalities
Post Feed: Share workout updates, achievements, and fitness tips.
Search & Filters: Search posts by username, title, or content.
Create Post: Share progress and experiences with the community.
Event Calendar: Discover and join fitness events on campus.
Messaging: Connect with personal trainers, peers, and organizations.

**Tech Stack**
Backend: Django 5.1.3, Python 3.12.8
Frontend: HTML5, CSS3, JavaScript (AJAX)
Database: SQLite (Development), PostgreSQL (Production)
Version Control: Git & GitHub

**Installation**
Clone the Repository:

bash
git clone https://github.com/yourusername/ufit.git
cd ufit
Create a Virtual Environment:

bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
Install Requirements:

bash
pip install -r requirements.txt
Apply Migrations:

bash
python manage.py makemigrations
python manage.py migrate
Run the Development Server:

bash
python manage.py runserver
Access the Project: Open http://127.0.0.1:8000 in your browser.

**Project Structure**
ufit/
│── base/
│   ├── migrations/
│   ├── templates/
│   │   ├── home.html
│   │   ├── post_form.html
│   │   └── chatpage.html
│   ├── static/
│   │   └── styles/
│   │       └── style.css
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── admin.py
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt

**Key Functionalities**
1. Registration & Authentication
Custom user profiles and secure logins.
2. Post Feed & Search
Create, view, and edit posts.
AJAX-powered live search by username, post title, or content.
3. Personal Trainers & Organizations
Search and connect with trainers and wellness organizations.
4. Event Calendar
Weekly events featuring fitness classes, training sessions, and wellness workshops.
5. Messaging System
In-app messaging between students, trainers, and organizations.
