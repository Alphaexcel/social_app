# social_app
Mini Social Media API


📌 Project Overview


This project is a backend API for a simple social media application where users can:


- Register accounts
- Create posts (with optional image upload)
- Like posts
- View posts by users


Built using FastAPI, SQLAlchemy ORM, and PostgreSQL.


---


🚀 Features


- User registration
- Create post with optional image upload
- View all posts
- View single post
- Update post
- Delete post
- Like a post
- View all users
- View posts by a specific user


---


🧱 Tech Stack


- Python
- FastAPI
- SQLAlchemy (ORM)
- PostgreSQL
- Uvicorn


---


📁 Project Structure


social_app/
│── app/
│   ├── api/
│   │   └── routes/
│   │       ├── users.py
│   │       └── posts.py
│   ├── core/
│   ├── models/
│   ├── schemas/
│   ├── database.py
│   ├── crud.py
│   ├── config.py
│   └── main.py
│
│── uploads/
│── .env
│── requirements.txt
│── venv/


---


⚙️ Setup Instructions


1. Clone the repository


git clone <your-repo-link>
cd social_app


2. Create virtual environment


python -m venv venv
venv\Scripts\activate


3. Install dependencies


pip install -r requirements.txt


4. Configure environment variables


Create a ".env" file:


DATABASE_URL=postgresql://username:password@localhost:5432/social_db


---


5. Run the application


uvicorn app.main:app --reload


---


📡 API Endpoints


👤 Users


- "POST /users/" → Register user
- "GET /users/" → Get all users
- "GET /users/{username}/posts" → Get user posts


---


📝 Posts


- "POST /posts/" → Create post
- "GET /posts/" → Get all posts
- "GET /posts/{post_id}" → Get single post
- "PUT /posts/{post_id}" → Update post
- "DELETE /posts/{post_id}" → Delete post
- "POST /posts/{post_id}/like" → Like post


---


📂 File Upload


Uploaded images are stored in the "uploads/" directory.


---


🧪 Testing


Use FastAPI Swagger UI:


http://127.0.0.1:8000/docs


---


⚠️ Notes


- PostgreSQL must be running locally
- Tables are auto-created on startup
- If schema changes occur, drop and recreate tables


---


👨‍💻 Author


OJIGBARE EXCEL OYINEMI
