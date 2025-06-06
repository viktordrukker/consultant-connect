import datetime
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Boolean, func, CheckConstraint, JSON
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class Rating(Base):
    """
    Database model for session ratings and feedback.
    """
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("sessions.id", ondelete="CASCADE"), unique=True, nullable=False, index=True)
    customer_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)  # User who gave the rating
    consultant_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)  # User who received the rating

    # Rating details
    overall_rating = Column(Integer, nullable=False)  # 1-5 star rating
    expertise_rating = Column(Integer)  # 1-5 rating for expertise
    communication_rating = Column(Integer)  # 1-5 rating for communication
    value_rating = Column(Integer)  # 1-5 rating for value
    
    # Feedback
    review_text = Column(Text)  # Written review
    improvement_suggestions = Column(Text)  # What could be improved
    would_recommend = Column(Boolean)  # Would recommend this consultant
    
    # Session quality feedback
    technical_issues = Column(Boolean, default=False)  # Any technical problems
    session_quality = Column(Integer)  # 1-5 rating for call quality
    
    # Metadata
    is_anonymous = Column(Boolean, default=False)  # Hide customer name in public reviews
    is_featured = Column(Boolean, default=False)  # Featured review
    helpful_votes = Column(Integer, default=0)  # How many found this helpful
    
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # Constraints
    __table_args__ = (
        CheckConstraint('overall_rating >= 1 AND overall_rating <= 5', name='overall_rating_check'),
        CheckConstraint('expertise_rating >= 1 AND expertise_rating <= 5', name='expertise_rating_check'),
        CheckConstraint('communication_rating >= 1 AND communication_rating <= 5', name='communication_rating_check'),
        CheckConstraint('value_rating >= 1 AND value_rating <= 5', name='value_rating_check'),
        CheckConstraint('session_quality >= 1 AND session_quality <= 5', name='session_quality_check'),
    )

    # Relationships
    session = relationship("Session", back_populates="rating")
    customer = relationship("User", foreign_keys=[customer_id])
    consultant = relationship("User", foreign_keys=[consultant_id])

    def __repr__(self):
        return f"<Rating(id={self.id}, session_id={self.session_id}, overall_rating={self.overall_rating})>"
