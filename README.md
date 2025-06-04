# Task-Manager-System
A task managment system made with django.

## Requirements
* Python 4
* Django 4
* Git
* HTML
* Bootstrap
* Venv (optional but highly recommended)

## Main features
* User authentication (login, register also logout) out of the box
* CRUD operations
* Bootstrap 5 static files
* Easy to undertand forms with validation.
* Implemented a communication between users on the topic of the task (comment system)

## Installation
1. Install the required libraries
```bash
pip install django
```

2. Clone the Repository
```bash
git clone https://github.com/xok9ty/dj_project.git
```
3. Set Up a Virtual Environment (Recommended)
```bash
venv\Scripts\activate
```

4. Run Migrations
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

## How to use
1. Start the Server
```bash
python manage.py runserver
```

2. Click the ''Register'' button and fill out the registration form, then log in. And you can use the task manager =)

## Note
If you try to edit someone else's task or comment, you will get a 403 - Forbidden error, which means you are not allowed to edit it. Don't touch other people's tasks and comment!!!
