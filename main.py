from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import uvicorn
from typing import List

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

class UserCreate(BaseModel):
    user_name: str = Field(min_length=1)
    user_email: str = Field(min_length=1)
    age: int = Field(gt=0, lt=110, default=None)
    recommendations: List[str] = []
    zip_code: str = Field(min_length=4, max_length=8, default=None)

@app.get("/")
def read_api(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@app.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.user_email == user.user_email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user_model = models.User(
        user_name=user.user_name,
        user_email=user.user_email,
        age=user.age,
        zip_code=user.zip_code
    )
    user_model.set_recommendations(user.recommendations)

    db.add(user_model)
    db.commit()
    db.refresh(user_model)

    return user_model

@app.put("/{user_id}")
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    user_model = db.query(models.User).filter(models.User.user_id == user_id).first()

    if user_model is None:
        raise HTTPException(status_code=404, detail=f"ID {user_id} : Does not exist")

    user_model.user_name = user.user_name
    user_model.user_email = user.user_email
    user_model.age = user.age
    user_model.set_recommendations(user.recommendations)
    user_model.zip_code = user.zip_code

    db.commit()
    db.refresh(user_model)

    return user_model
