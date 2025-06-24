Late Show API Challenge
A Flask REST API for managing a Late Night TV show — featuring guests, episodes, appearances, and secure user authentication with JWT.
Built with PostgreSQL, structured with MVC, and fully tested with Postman.

 Project Structure
pgsql
Copy code
.
 server/
  app.py
   config.py
  seed.py
  models/
 __init__.py
 guest.py
  episode.py
 appearance.py
 user.py
controllers/
 __init__.py
 guest_controller.py
 episode_controller.py
 appearance_controller.py
 auth_controller.py
 migrations/
 README.md
 Tech Stack
Flask

PostgreSQL

SQLAlchemy

Flask-Migrate

Flask-JWT-Extended

Postman for API testing

 Setup Instructions
1️ Clone the repository
bash
Copy code
git clone https://github.com/<your-username>/late-show-api-challenge.git
cd late-show-api-challenge
2️ Install dependencies and activate virtual environment
bash
Copy code
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary
pipenv shell
3️ Create the PostgreSQL database
sql
Copy code
CREATE DATABASE late_show_db;
4 Configure server/config.py
python
Copy code
SQLALCHEMY_DATABASE_URI = "postgresql://<username>:<password>@localhost:5432/late_show_db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET_KEY = "<your_secret_key>"
5️ Run migrations and seed data
bash
Copy code
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial migration"
flask db upgrade
python -m server.seed
6️ Run the server
bash
Copy code
flask run
 Authentication
Uses JWT (JSON Web Tokens) to protect sensitive endpoints.

Action	Route	Auth Required
Register	POST /register	❌
Login	POST /login	❌
Protected Routes	✅ Use Authorization: Bearer <JWT>	

 API Routes
Route	Method	Auth Required	Description
/register	POST	❌	Register a new user
/login	POST	❌	Log in and receive JWT
/episodes	GET	❌	List all episodes
/episodes/<int:id>	GET	❌	Get a single episode with appearances
/episodes/<int:id>	DELETE	✅	Delete an episode and its appearances
/guests	GET	❌	List all guests
/appearances	POST	✅	Create a new appearance

 Sample Authentication Flow
1️ Register
h
Copy code
POST /register
Content-Type: application/json

{
  "username": "newuser",
  "password": "password123"
}
2️ Login
http
Copy code
POST /login
Content-Type: application/json

{
  "username": "newuser",
  "password": "password123"
}
Response:

json
Copy code
{
  "access_token": "<JWT_TOKEN>"
}
3️ Use the token
Include it in headers for protected requests:

makefile
Copy code
Authorization: Bearer <JWT_TOKEN>