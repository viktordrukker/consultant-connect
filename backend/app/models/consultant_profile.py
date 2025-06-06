import datetime
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, JSON, Boolean, func
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class ConsultantProfile(Base):
    """
    Database model for consultant profiles.
    Enhanced for AI-driven instant matching platform.
    """
    __tablename__ = "consultant_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False, index=True)
    
    # Basic profile info
    headline = Column(String(255), index=True)  # Short professional title
    bio = Column(Text)  # Longer description
    expertise_tags = Column(JSON)  # ["python", "fastapi", "aws", "startup", "marketing"]
    
    # Pricing and availability
    hourly_rate = Column(Integer, nullable=False)  # Rate in cents for consistency
    is_available = Column(Boolean, default=True, index=True)  # Real-time availability toggle
    
    # AI matching optimization
    response_time_avg = Column(Integer, default=300)  # Average response time in seconds
    success_rate = Column(Integer, default=100)  # Success rate percentage (0-100)
    total_sessions = Column(Integer, default=0)  # Total completed sessions
    total_earnings = Column(Integer, default=0)  # Total earnings in cents
    
    # Quality metrics for AI ranking
    average_rating = Column(Integer, default=50)  # Average rating * 10 (1-50 scale)
    trust_score = Column(Integer, default=70)  # AI-calculated trust score (0-100)
    specialization_score = Column(JSON)  # Expertise strength per tag
    
    # LinkedIn integration
    linkedin_url = Column(String)
    linkedin_data = Column(JSON)  # Imported LinkedIn profile data
    
    # Profile status
    is_verified = Column(Boolean, default=False)
    verification_notes = Column(String)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # Relationship back to the User
    user = relationship("User", back_populates="consultant_profile")

    def __repr__(self):
        return f"<ConsultantProfile(id={self.id}, user_id={self.user_id}, headline='{self.headline}', available={self.is_available})>"
