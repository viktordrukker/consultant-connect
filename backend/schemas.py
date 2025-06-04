from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    first_name: Optional[str]
    last_name: Optional[str]
    role: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    first_name: Optional[str]
    last_name: Optional[str]
    role: str

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class ConsultantProfileIn(BaseModel):
    headline: Optional[str] = None
    bio: Optional[str] = None
    expertise_tags: Optional[str] = None
    hourly_rate: Optional[float] = None

class ConsultantProfileOut(ConsultantProfileIn):
    id: int
    user_id: int
    class Config:
        orm_mode = True

class AvailabilitySlotIn(BaseModel):
    start_time: datetime
    end_time: datetime

class AvailabilitySlotOut(AvailabilitySlotIn):
    id: int
    is_booked: bool
    class Config:
        orm_mode = True
