import enum
import datetime
from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey, func, JSON
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class MatchStatus(str, enum.Enum):
    """
    Enum for question-consultant match statuses.
    """
    PENDING = "pending"     # Question sent to consultant, waiting for response
    ACCEPTED = "accepted"   # Consultant accepted the question
    DECLINED = "declined"   # Consultant declined the question
    EXPIRED = "expired"     # Consultant didn't respond in time

class QuestionMatch(Base):
    """
    Database model for tracking consultant matches to customer questions.
    Replaces complex booking system with simple matching logic.
    """
    __tablename__ = "question_matches"

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.id", ondelete="CASCADE"), nullable=False, index=True)
    consultant_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    
    # Match scoring and selection
    match_score = Column(Integer, nullable=False)  # AI-calculated match score (0-100)
    status = Column(Enum(MatchStatus), default=MatchStatus.PENDING, nullable=False, index=True)
    response_deadline = Column(DateTime(timezone=True))  # When match expires
    
    # Consultant response
    consultant_response = Column(String)  # Brief response when accepting/declining
    estimated_duration = Column(Integer)  # Consultant's estimate in minutes
    
    # Metadata
    sent_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    responded_at = Column(DateTime(timezone=True))
    
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # Relationships
    question = relationship("Question")
    consultant = relationship("User", foreign_keys=[consultant_id])

    def __repr__(self):
        return f"<QuestionMatch(id={self.id}, question_id={self.question_id}, consultant_id={self.consultant_id}, status='{self.status}', score={self.match_score})>"
