
# JobTrack – Job Application Tracker

A Django-based web application to organize and track job applications in one place.

## About the Project

JobTrack helps job seekers manage their job applications through a simple dashboard. Users can add applications, update their details, track application statuses, and search or filter records.

## Features

- Dashboard with total application statistics
- Track Applied, Interview, Selected, and Rejected statuses
- Add new job applications
- Edit existing application details
- Delete applications
- Search by company name or job role
- Filter applications by status
- Sort applications by application date

## Technologies Used

- Python
- Django
- HTML
- CSS
- SQLite
- Git and GitHub

## Project Structure

```text
job-application-tracker/
├── config/
├── jobs/
│   ├── migrations/
│   ├── templates/
│   │   └── jobs/
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── .gitignore
├── manage.py
└── README.md
```

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Rohini-saindane-Dev/JobTrack.git
cd JobTrack
```

### 2. Create and activate a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Django

```bash
python -m pip install django
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Future Improvements

- User authentication
- Application deadline reminders
- Dashboard charts and analytics
- Live deployment

## Author

Rohini Saindane

GitHub: https://github.com/Rohini-saindane-Dev
