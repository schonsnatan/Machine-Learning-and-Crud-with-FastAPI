from typing import Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    name: Optional[str] = None
    area: Optional[str] = None
    job_description: Optional[str] = None
    role: Optional[int] = None
    salary: Optional[float] = None
    is_active: Optional[bool] = None
    last_evaluation: Optional[str] = None

class UserCreate(UserBase):
    id: int  
    name: str

class UserUpdate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
