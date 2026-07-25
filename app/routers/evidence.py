from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Evidence)
def create_evidence(evidence: schemas.EvidenceCreate, db: Session = Depends(get_db)):
    db_evidence = models.Evidence(**evidence.dict())
    db.add(db_evidence)
    db.commit()
    db.refresh(db_evidence)
    return db_evidence

@router.get("/{evidence_id}", response_model=schemas.Evidence)
def get_evidence(evidence_id: int, db: Session = Depends(get_db)):
    evidence = db.query(models.Evidence).filter(models.Evidence.id == evidence_id).first()
    if not evidence:
        raise HTTPException(status_code=404, detail="Evidence not found")
    return evidence

@router.get("/", response_model=list[schemas.Evidence])
def list_evidence(query_id: int = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query_filter = db.query(models.Evidence)
    if query_id:
        query_filter = query_filter.filter(models.Evidence.query_id == query_id)
    evidence = query_filter.offset(skip).limit(limit).all()
    return evidence

@router.delete("/{evidence_id}")
def delete_evidence(evidence_id: int, db: Session = Depends(get_db)):
    evidence = db.query(models.Evidence).filter(models.Evidence.id == evidence_id).first()
    if not evidence:
        raise HTTPException(status_code=404, detail="Evidence not found")
    db.delete(evidence)
    db.commit()
    return {"message": "Evidence deleted"}