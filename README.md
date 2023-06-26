# KNK Studios Backend

This is the backend component of the KNK Studios project, built using Django and Django REST Framework. It provides an API for interacting with the application's data.

## Features

- User authentication and authorization using JWT (JSON Web Token) for secure API access.
- Swagger documentation for easy API exploration and testing.
- CRUD operations for various models/entities of the application.

## Installation

1. Clone the repository:
   ```
   git clone <repository_url>
   ```

2. Navigate to the project directory:
   ```
   cd knk-studios-backend
   ```

3. Create a virtual environment:
   ```
   python -m venv env
   ```

4. Activate the virtual environment:
   - On Windows:
     ```
     env\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source env/bin/activate
     ```

5. Install the project dependencies:
   ```
   pip install -r requirements.txt
   ```

6. Perform database migrations:
   ```
   python manage.py migrate
   ```

7. Create a superuser account:
   ```
   python manage.py createsuperuser
   ```

8. Start the development server:
   ```
   python manage.py runserver
   ```

## API Endpoints

The following API endpoints are available:

- **Authentication:**
  - `POST /api/token/`: Obtain a JWT token by providing valid credentials.
  - `POST /api/token/refresh/`: Refresh an existing JWT token.

- **User Profile:**
  - `GET /api/profile/`: Retrieve the authenticated user's profile information.
  - `PUT /api/profile/`: Update the authenticated user's profile information.

- **Other Entities:** (Add more as needed)
  - `GET /api/entity/`: Retrieve a list of entities.
  - `POST /api/entity/`: Create a new entity.
  - `GET /api/entity/{id}/`: Retrieve a specific entity.
  - `PUT /api/entity/{id}/`: Update a specific entity.
  - `DELETE /api/entity/{id}/`: Delete a specific entity.

For more detailed API documentation and interactive exploration, visit the Swagger UI page available at `/swagger/`.

## Configuration

The project's configuration can be found in the following files:

- `settings.py`: Contains the Django settings, including database configuration, installed apps, middleware, and more.
- `urls.py`: Defines the URL routing for the project's API endpoints.

## Contributing

Thank you for considering contributing to the KNK Studios Backend project! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as per the terms of the license.
