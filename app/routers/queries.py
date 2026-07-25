from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Query)
def create_query(query: schemas.QueryCreate, db: Session = Depends(get_db)):
    db_query = models.Query(**query.dict())
    db.add(db_query)
    db.commit()
    db.refresh(db_query)
    return db_query

@router.get("/{query_id}", response_model=schemas.Query)
def get_query(query_id: int, db: Session = Depends(get_db)):
    query = db.query(models.Query).filter(models.Query.id == query_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="Query not found")
    return query

@router.get("/", response_model=list[schemas.Query])
def list_queries(brief_id: int = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query_filter = db.query(models.Query)
    if brief_id:
        query_filter = query_filter.filter(models.Query.brief_id == brief_id)
    queries = query_filter.offset(skip).limit(limit).all()
    return queries

@router.delete("/{query_id}")
def delete_query(query_id: int, db: Session = Depends(get_db)):
    query = db.query(models.Query).filter(models.Query.id == query_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="Query not found")
    db.delete(query)
    db.commit()
    return {"message": "Query deleted"}