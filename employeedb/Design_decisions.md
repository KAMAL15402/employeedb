# Design Decisions - EmployeeDB Backend Task

## Why Django and Django REST Framework?

- Django is a high-level Python framework that provides quick development with a clean design.
- Django REST Framework (DRF) extends Django to build powerful APIs easily.
- Built-in features like ORM, admin panel, and authentication simplify backend development.
- DRF automatically handles API serialization, validation, and routing cleanly.

## Why PostgreSQL?

- PostgreSQL is a robust, scalable, open-source relational database.
- It is production-ready, ACID-compliant, and supports complex queries and indexing.
- Preferred over SQLite for real-world production applications.

## Project Structure and Practices

- Separate app (`employee`) created to manage all employee-related functionality.
- Environment variables (`.env` file) used for sensitive settings like database credentials.
- Basic authentication added for API security.
- Pagination, filtering, and ordering enabled for better API performance.
- Health endpoint `/health/` added to monitor application status.
- Swagger UI (`drf-yasg`) integrated for easy API exploration and documentation.
- Employee data generation automated using Faker for quick testing.

## Optional Enhancements Done

- Export employees to CSV (`/api/employees/export/`).
- Additional model Attendance created and APIs exposed.
- Unit testing added to verify model creation.
- README.md and this Design Decisions file added for better project clarity.

## Future Improvements

- Dockerize the project for easy deployment.
- Add JWT Authentication.
- Add user roles (admin, employee).
- Setup CI/CD pipeline with GitHub Actions.

