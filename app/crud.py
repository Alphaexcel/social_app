from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models import User , Post

def get_user(db: Session, username: str):
    return db.query(User).filter(func.lower(User.username) == username).first()

def get_users(db: Session):
    return db.query(User).all()

def create_user(db: Session, username: str):
    user = User(username=username)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def create_post(db: Session, user, title: str, content: str, image_path=None):
    post = Post(
        title=title,
        content=content,
        image=image_path,
        owner=user
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def get_posts(db: Session):
    return db.query(Post).all()

def get_post(db: Session, post_id: int):
    return db.get(Post, post_id)

def get_user_posts(db: Session, username: str):
    user = get_user(db, username)
    if not user:
        return None
    return user.posts

def like_post(db: Session, post_id: int):
    post = db.get(Post, post_id)
    if post:
        post.likes += 1
        db.commit()
        db.refresh(post)
    return post


# Update post 
def update_post(db: Session, post_id:int, title=None, content=None):
    post = db.get(Post, post_id)
    if not post:
        return None
    
    if title is not None:
        post.title = title
    if content is not None:
        post.content = content

    db.commit()
    db.refresh(post)
    return post

# Delete post 
def delete_post(db: Session, post_id: int):
    post = db.get(Post, post_id)
    if not post:
        return None
    
    db.delete(post)
    db.commit()
    return post
