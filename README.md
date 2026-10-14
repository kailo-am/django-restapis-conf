# Django REST API Project

This project is a Django-based REST API application for managing student and employee records. It demonstrates common Django REST Framework patterns such as function-based views, model serializers, CRUD operations, and a ViewSet-based employee API.

## Features

- Student CRUD API with JSON responses
- Employee API powered by DRF `ModelViewSet`
- Search and filtering support for employee records
- Pagination enabled by default
- SQLite database for local development
- Django admin support

## Tech Stack

- Python
- Django
- Django REST Framework
- django-filter
- SQLite

## Project Structure

```text
django_rest_project/
├── api/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── django_rest_main/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── employees/
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── students/
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt (if added later)
```

## Models

### Student

Fields:
- `student_id` - unique student identifier
- `name` - student full name
- `branch` - academic branch or specialization

### Employee

Fields:
- `name`
- `email` - unique email address
- `position`
- `department`

## API Endpoints

### Student endpoints

- `GET /students/` - list all students
- `POST /students/` - create a new student
- `GET /students/<id>/` - get a specific student
- `PUT /students/<id>/` - update a student
- `DELETE /students/<id>/` - delete a student

### API v1 endpoints

- `GET /api/v1/students/` - list students through API app routes
- `POST /api/v1/students/` - create a student
- `GET /api/v1/students/<id>/` - fetch a student
- `PUT /api/v1/students/<id>/` - update a student
- `DELETE /api/v1/students/<id>/` - delete a student
- `GET /api/v1/employees/` - list employees
- `POST /api/v1/employees/` - create an employee
- `GET /api/v1/employees/<id>/` - fetch an employee
- `PUT /api/v1/employees/<id>/` - update an employee
- `DELETE /api/v1/employees/<id>/` - delete an employee

## Setup Instructions

1. Clone the repository

```bash
git clone <repository-url>
cd django_rest_project
```

2. Create and activate a virtual environment

```bash
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
```

3. Install dependencies

```bash
pip install django djangorestframework django-filter
```

4. Apply database migrations

```bash
python manage.py migrate
```

5. Create a superuser (optional, for admin access)

```bash
python manage.py createsuperuser
```

6. Run the development server

```bash
python manage.py runserver
```

Then open the app in a browser at:

```text
http://127.0.0.1:8000/
```

## Admin Panel

You can access Django's admin panel at:

```text
http://127.0.0.1:8000/admin/
```

Use the superuser credentials created above to log in.

## Example API Requests

### Create a student

```bash
curl -X POST http://127.0.0.1:8000/api/v1/students/ \
  -H "Content-Type: application/json" \
  -d '{"student_id": "S101", "name": "Alice", "branch": "CSE"}'
```

### List employees

```bash
curl http://127.0.0.1:8000/api/v1/employees/
```

## Notes

- The project currently uses SQLite in development mode.
- The app is a learning/demo project focused on understanding Django REST Framework fundamentals.
- You can modify the settings in `django_rest_main/settings.py` to use a production database and other environment-specific configuration.

## License

This project does not currently declare a specific license.
