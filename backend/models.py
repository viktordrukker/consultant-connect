from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from datetime import datetime

from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    role = Column(String, nullable=False)  # 'seeker' or 'consultant'
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    profile = relationship("ConsultantProfile", back_populates="user", uselist=False)

class ConsultantProfile(Base):
    __tablename__ = "consultant_profiles"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)
    headline = Column(String)
    bio = Column(String)
    expertise_tags = Column(String)
    hourly_rate = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user = relationship("User", back_populates="profile")
    availability = relationship("AvailabilitySlot", back_populates="consultant")

class AvailabilitySlot(Base):
    __tablename__ = "availability_slots"
    id = Column(Integer, primary_key=True)
    consultant_id = Column(Integer, ForeignKey('consultant_profiles.id'))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    is_booked = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    consultant = relationship("ConsultantProfile", back_populates="availability")
