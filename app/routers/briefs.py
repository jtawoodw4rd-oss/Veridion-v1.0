from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Brief)
def create_brief(brief: schemas.BriefCreate, db: Session = Depends(get_db)):
    db_brief = models.Brief(**brief.dict())
    db.add(db_brief)
    db.commit()
    db.refresh(db_brief)
    return db_brief

@router.get("/{brief_id}", response_model=schemas.Brief)
def get_brief(brief_id: int, db: Session = Depends(get_db)):
    brief = db.query(models.Brief).filter(models.Brief.id == brief_id).first()
    if not brief:
        raise HTTPException(status_code=404, detail="Brief not found")
    return brief

@router.get("/", response_model=list[schemas.Brief])
def list_briefs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    briefs = db.query(models.Brief).offset(skip).limit(limit).all()
    return briefs

@router.delete("/{brief_id}")
def delete_brief(brief_id: int, db: Session = Depends(get_db)):
    brief = db.query(models.Brief).filter(models.Brief.id == brief_id).first()
    if not brief:
        raise HTTPException(status_code=404, detail="Brief not found")
    db.delete(brief)
    db.commit()
    return {"message": "Brief deleted"}