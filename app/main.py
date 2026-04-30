from fastapi import FastAPI 
from app.database import engine, Base
from app import models

from app.api.routes import users, posts 

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mini Social Media API")

app.include_router(users.router)
app.include_router(posts.router)