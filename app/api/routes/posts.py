from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session 
import shutil
import os

from app.database import SessionLocal
from app import crud
from app.schemas import PostUpdate

router = APIRouter(prefix="/posts", tags=["Posts"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", status_code=201)
def create_post(
    username: str = Form(...),
    title: str = Form(...),
    content: str = Form(...),
    image: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    user = crud.get_user(db, username)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
        
    
    image_path = None

    if image:
        file_path = f"{UPLOAD_DIR}/{image.filename}"
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        image_path = file_path

    return crud.create_post(db, user, title, content, image_path)

@router.get("/", status_code=200)
def get_posts(db: Session = Depends(get_db)):
    return crud.get_posts(db)

@router.get("/{post_id}", status_code=200)
def like_post(post_id: int, db: Session = Depends(get_db)):

    if post_id <= 0:
        raise HTTPException(
            status_code=400,
            detail="Invalid post ID"
        )

    post = crud.like_post(db, post_id)

    if not post:
        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )
    return post

@router.get("/{post_id}/like", status_code=200)
def get_single_post(post_id: int, db:Session = Depends(get_db)):
    
    if post_id <= 0:
        raise HTTPException(
            status_code=400,
            detail="Invalid post ID"
        )
    
    post = crud.get_POST(db, post_id)

    if not post:
        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )
    post.likes += 1
    db.commit()
    db.refresh(post)
    return post

@router.put("/{post_id}", status_code=200)
def update_post(post_id: int, data: PostUpdate, db: Session = Depends(get_db)):
    
    if post_id <= 0:
        raise HTTPException(
            status_code=400,
            detail="Invalid post ID"
        )
    
    post = crud.get_POST(db, post_id)

    if not post:
        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )
    if data.title is not None:
        post.title = data.title
    
    if data.content is not None:
        post.content = data.content

    db.commit()
    db.refresh(post)
    return post

@router.delete("/{post_id}", status_code=200)
def delete_post(post_id: int, db: Session = Depends(get_db)):

    if post_id <= 0:
        raise HTTPException(
            status_code=400,
            detail="Invalid post ID"
        )

    post = crud.delete_post(db, post_id)

    if not post:
        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )
    db.delete(post)
    db.commit()
    return {"message": "Post deleted successfully"}