# EmployeeDB 

This project is a Django REST Framework application for generating, storing, and visualizing Employee data with PostgreSQL database.

---

## ✅ Features

- Generate synthetic employee data using Faker.
- Store employee records securely in PostgreSQL.
- REST APIs for listing and creating employees.
- Filtering, searching, and pagination support for APIs.
- Basic authentication enabled.
- Swagger UI integration for API documentation.
- API rate limiting (throttling) enabled for abuse protection.

---

## ⚙️ Setup Instructions (Mac/Linux)

1. Clone the Repository**
   ```bash
   git clone <your-github-repo-link>
   cd employeedb

2. Create Virtual Environment
    
    python3 -m venv env
    source env/bin/activate

3. Install Requirement
    
    pip install -r requirements.txt

4. Configure PostgreSQL

    Create a database called employeedb
    Create a PostgreSQL user with username postgres and a password you like.

5. Update settings.py with your PostgreSQL credentials

6. Run Migrations

    python manage.py makemigrations
    python manage.py migrate

7. Seed Database

    python manage.py seed

8. Run Database

    python manage.py runserver

9. Access API

    List/Create Employees: http://127.0.0.1:8000/api/employees/
    Swagger UI: http://127.0.0.1:8000/swagger/
    Health Check: http://127.0.0.1:8000/health/



## API ENDPOINTS

GET	/api/employees/	List all employees
POST /api/employees/ Create a new employee record
GET	/api/employees/export/ Export employees as CSV
GET	/api/attendance/ List all attendance records
POST /api/attendance/ Create an attendance record
GET	/swagger/Swagger UI documentation
GET	/health/Health check endpoint

## Tech Stack
Django

Django REST Framework

PostgreSQL

Faker

Swagger