from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Intent)
def create_intent(intent: schemas.IntentCreate, db: Session = Depends(get_db)):
    db_intent = models.Intent(**intent.dict())
    db.add(db_intent)
    db.commit()
    db.refresh(db_intent)
    return db_intent

@router.get("/{intent_id}", response_model=schemas.Intent)
def get_intent(intent_id: int, db: Session = Depends(get_db)):
    intent = db.query(models.Intent).filter(models.Intent.id == intent_id).first()
    if not intent:
        raise HTTPException(status_code=404, detail="Intent not found")
    return intent

@router.get("/", response_model=list[schemas.Intent])
def list_intents(brief_id: int = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query = db.query(models.Intent)
    if brief_id:
        query = query.filter(models.Intent.brief_id == brief_id)
    intents = query.offset(skip).limit(limit).all()
    return intents

@router.delete("/{intent_id}")
def delete_intent(intent_id: int, db: Session = Depends(get_db)):
    intent = db.query(models.Intent).filter(models.Intent.id == intent_id).first()
    if not intent:
        raise HTTPException(status_code=404, detail="Intent not found")
    db.delete(intent)
    db.commit()
    return {"message": "Intent deleted"}