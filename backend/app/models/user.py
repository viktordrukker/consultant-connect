import enum
import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum, func
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class UserRole(str, enum.Enum):
    """
    Enum for user roles in our AI-driven platform.
    """
    CUSTOMER = "customer"      # Renamed from SEEKER for clarity
    CONSULTANT = "consultant"
    ADMIN = "admin"

class User(Base):
    """
    Database model for users (customers and consultants).
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    role = Column(Enum(UserRole), nullable=False, index=True)
    is_active = Column(Boolean(), default=True)
    
    # Enhanced user data for AI platform
    profile_picture_url = Column(String)
    timezone = Column(String, default="UTC")
    preferred_language = Column(String, default="en")
    phone_number = Column(String)
    
    # Platform metrics
    total_sessions = Column(Integer, default=0)
    last_active_at = Column(DateTime(timezone=True))
    
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # Relationships for our simplified AI-driven platform
    consultant_profile = relationship("ConsultantProfile", back_populates="user", uselist=False, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(id={self.id}, email='{self.email}', role='{self.role}')>"

    @property
    def full_name(self):
        """Return the user's full name."""
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.first_name or self.last_name or self.email.split('@')[0]
