import enum
import datetime
from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey, Boolean, Float, func, JSON
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class SessionStatus(str, enum.Enum):
    """
    Enum for session statuses.
    """
    PENDING = "pending"         # Session created, waiting to start
    ACTIVE = "active"           # Video call in progress
    COMPLETED = "completed"     # Session finished successfully
    CANCELLED = "cancelled"     # Session cancelled before start
    NO_SHOW = "no_show"         # Consultant or customer didn't show up
    ABANDONED = "abandoned"     # Session ended before 10 minutes

class Session(Base):
    """
    Database model for video consultation sessions.
    """
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.id", ondelete="CASCADE"), unique=True, nullable=False, index=True)
    customer_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    consultant_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    
    # Session details
    status = Column(Enum(SessionStatus), default=SessionStatus.PENDING, nullable=False, index=True)
    hourly_rate = Column(Integer, nullable=False)  # Rate in cents at time of booking
    
    # Timing
    scheduled_start = Column(DateTime(timezone=True))  # When session should start
    actual_start = Column(DateTime(timezone=True))     # When video call actually started
    actual_end = Column(DateTime(timezone=True))       # When video call ended
    duration_minutes = Column(Integer)                 # Calculated session duration
    
    # Billing
    is_billable = Column(Boolean, default=False)      # >10 minutes = billable
    amount_charged = Column(Integer)                   # Amount charged in cents
    commission_amount = Column(Integer)                # Platform commission in cents
    consultant_payout = Column(Integer)                # Amount paid to consultant in cents
    
    # Video call details
    room_id = Column(String, unique=True, index=True)  # Video call room identifier
    recording_url = Column(String)                     # Recording storage URL
    
    # Quality metrics
    connection_quality = Column(JSON)                  # Connection quality data
    customer_satisfaction = Column(Integer)            # 1-5 rating from customer
    consultant_notes = Column(String)                  # Private notes for consultant
    
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # Relationships
    question = relationship("Question", back_populates="session")
    customer = relationship("User", foreign_keys=[customer_id])
    consultant = relationship("User", foreign_keys=[consultant_id])
    rating = relationship("Rating", back_populates="session", uselist=False)

    def __repr__(self):
        return f"<Session(id={self.id}, customer_id={self.customer_id}, consultant_id={self.consultant_id}, status='{self.status}')>"
