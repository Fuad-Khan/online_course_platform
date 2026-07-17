# Online Course Platform

A Django-based Online Course Platform developed as an assignment.

## Features

- Instructor Management
- Course Management
- Student Registration
- Course Enrollment
- Course Reviews
- Django Authentication
- Login & Logout
- Password Change
- Password Reset
- Login Required My Enrollments Page
- ORM Queries
- Raw SQL Query

## Models

- Instructor
- Course
- Student
- Enrollment
- Review
- BaseInfo (Abstract Model)

## Technologies Used

- Python 3.x
- Django 5.x
- SQLite3

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/online-course-platform.git
```

### Enter Project

```bash
cd online-course-platform
```

### Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

Visit

```
http://127.0.0.1:8000/
```

Admin

```
http://127.0.0.1:8000/admin/
```

---

## ORM Queries Implemented

- select_related()
- prefetch_related()
- annotate()
- aggregate()
- ordering()
- slicing()
- Raw SQL

---

## Authentication

- Registration
- Login
- Logout
- Password Change
- Password Reset
- LoginRequiredMixin

---

## Author

Fuad Khan