from fastapi import APIRouter , Depends, Form, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud

router = APIRouter(prefix="/users", tags=["users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", status_code=201)
def register_user(username: str = Form(...), db: 
Session = Depends(get_db)):
    
    username = username.strip()

    if not username:
        raise HTTPException(
            status_code=400, 
            detail="Username cannot be empty")
    
    existing_user =  crud.get_user(db, username)
    if existing_user:
        raise HTTPException(
            status_code=400, 
            detail="Username already exists")
    return crud.create_user(db, username)


@router.get("/{username}/posts", status_code=200)
def get_user_posts(username: str, db: Session = Depends(get_db)):

    user = crud.get_user(db, username)

    if not user:
        raise HTTPException(
            status_code=404, 
            detail="User not found")
    return user.posts

@router.get("/", status_code=200) 
def get_all_users(db: Session = Depends(get_db)):
    return crud.get_users(db)