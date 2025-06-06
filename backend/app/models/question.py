import enum
import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, ForeignKey, Boolean, func, JSON
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class QuestionStatus(str, enum.Enum):
    """
    Enum for question statuses.
    """
    OPEN = "open"           # Waiting for consultant to accept
    MATCHED = "matched"     # Consultant accepted, preparing session
    IN_SESSION = "in_session"  # Active video call
    COMPLETED = "completed" # Session finished
    CANCELLED = "cancelled" # Cancelled before session
    EXPIRED = "expired"     # No consultant accepted in time

class UrgencyLevel(str, enum.Enum):
    """
    Enum for question urgency levels.
    """
    LOW = "low"         # Can wait hours/days
    MEDIUM = "medium"   # Need help within hours
    HIGH = "high"       # Need help ASAP
    URGENT = "urgent"   # Emergency consultation

class Question(Base):
    """
    Database model for customer questions that need consultant expertise.
    """
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    
    # Question content
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=False)
    expertise_tags = Column(JSON)  # Required expertise areas
    urgency = Column(Enum(UrgencyLevel), default=UrgencyLevel.MEDIUM, nullable=False, index=True)
    
    # Status and matching
    status = Column(Enum(QuestionStatus), default=QuestionStatus.OPEN, nullable=False, index=True)
    max_budget = Column(Integer)  # Maximum customer willing to pay (in cents)
    expires_at = Column(DateTime(timezone=True))  # Auto-expire if no response
    
    # AI matching data
    processed_keywords = Column(JSON)  # Extracted keywords for matching
    match_score_threshold = Column(Integer, default=70)  # Minimum match score
    
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # Relationships
    customer = relationship("User", foreign_keys=[customer_id])
    session = relationship("Session", back_populates="question", uselist=False)

    def __repr__(self):
        return f"<Question(id={self.id}, customer_id={self.customer_id}, status='{self.status}', urgency='{self.urgency}')>"
