from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from typing import List

from database import Base, engine
from models import User, ConsultantProfile, AvailabilitySlot
from schemas import UserCreate, UserOut, Token, ConsultantProfileIn, ConsultantProfileOut, AvailabilitySlotIn, AvailabilitySlotOut
from deps import get_db, get_current_user
from auth import get_password_hash, verify_password, create_access_token

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Consultant Connect MVP")

@app.post('/register', response_model=Token)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user_in.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    user = User(
        email=user_in.email,
        hashed_password=get_password_hash(user_in.password),
        first_name=user_in.first_name,
        last_name=user_in.last_name,
        role=user_in.role,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    token = create_access_token({"sub": user.id})
    return Token(access_token=token)

@app.post('/login', response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_access_token({"sub": user.id})
    return Token(access_token=token)

@app.get('/me', response_model=UserOut)
def read_current_user(current_user: User = Depends(get_current_user)):
    return current_user

@app.put('/consultants/me/profile', response_model=ConsultantProfileOut)
def upsert_profile(profile_in: ConsultantProfileIn, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    if current_user.role != 'consultant':
        raise HTTPException(status_code=403, detail="Only consultants can have profiles")
    profile = db.query(ConsultantProfile).filter(ConsultantProfile.user_id == current_user.id).first()
    if profile:
        for field, value in profile_in.dict(exclude_unset=True).items():
            setattr(profile, field, value)
    else:
        profile = ConsultantProfile(user_id=current_user.id, **profile_in.dict(exclude_unset=True))
        db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile

@app.get('/consultants/{consultant_id}/profile', response_model=ConsultantProfileOut)
def get_profile(consultant_id: int, db: Session = Depends(get_db)):
    profile = db.query(ConsultantProfile).filter(ConsultantProfile.user_id == consultant_id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile

@app.post('/consultants/me/availability', response_model=List[AvailabilitySlotOut])
def set_availability(slots: List[AvailabilitySlotIn], current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    if current_user.role != 'consultant':
        raise HTTPException(status_code=403, detail="Only consultants can set availability")
    profile = db.query(ConsultantProfile).filter(ConsultantProfile.user_id == current_user.id).first()
    if not profile:
        raise HTTPException(status_code=400, detail="Profile missing")
    created = []
    for slot_in in slots:
        slot = AvailabilitySlot(consultant_id=profile.id, **slot_in.dict())
        db.add(slot)
        created.append(slot)
    db.commit()
    for slot in created:
        db.refresh(slot)
    return created

@app.get('/consultants/{consultant_id}/availability', response_model=List[AvailabilitySlotOut])
def get_availability(consultant_id: int, db: Session = Depends(get_db)):
    slots = db.query(AvailabilitySlot).join(ConsultantProfile).filter(ConsultantProfile.user_id == consultant_id, AvailabilitySlot.is_booked == False).all()
    return slots

@app.get('/consultants', response_model=List[ConsultantProfileOut])
def list_consultants(search: str | None = None, db: Session = Depends(get_db)):
    query = db.query(ConsultantProfile)
    if search:
        like = f"%{search}%"
        query = query.filter((ConsultantProfile.headline.ilike(like)) | (ConsultantProfile.bio.ilike(like)) | (ConsultantProfile.expertise_tags.ilike(like)))
    return query.all()
