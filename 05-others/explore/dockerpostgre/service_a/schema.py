from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id: int
    name: str
    
    
class UserResponse(BaseModel):
    id: int
    name: str
    
    class Config:
        orm_mode = True

class UserAllResponse(BaseModel):
    users: List[User]
    status: str = "ok"
    
    model_config = {
        "from_attributes": True
    }