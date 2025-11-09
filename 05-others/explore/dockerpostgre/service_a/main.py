from fastapi import FastAPI, Depends
from schema import User, UserResponse, UserAllResponse
from models import UserModel, Base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
import time
from sqlalchemy.exc import OperationalError

app = FastAPI()

POSTGRE_URI = "postgresql://admin:admin@database:5432/demodb"

engine = create_engine(url=POSTGRE_URI)

## wrapper for create_all tables, kasi yung Base.metadata.create_all() immediately runs, kailangan ng delay to make sure db is already created
## and init. For experiment only
for _ in range(10):
    try:
        Base.metadata.create_all(bind=engine)
        break
    except OperationalError:
        print("Database not ready, retrying in 5s...")
        time.sleep(5)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.get("/")
def home():
    return {
        "message": "hallo, api running ok",
        "status": "ok"
    }
    
@app.post("/create_user", response_model=UserResponse)
def create_user(user: User, db: Session = Depends(get_db)):
    
    new_user = UserModel(
        id=user.id, name=user.name
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return UserResponse(
        id=new_user.id,
        name=new_user.name
    )

@app.get("/get_users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(UserModel).all()
    
    return UserAllResponse(
        users=[User.model_validate(u, from_attributes=True) for u in users], 
        status="Data was retrieve, status ok"
    )
    