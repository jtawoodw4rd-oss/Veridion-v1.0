from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Brief(Base):
    __tablename__ = "briefs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    intents = relationship("Intent", back_populates="brief")
    queries = relationship("Query", back_populates="brief")

class Intent(Base):
    __tablename__ = "intents"
    id = Column(Integer, primary_key=True, index=True)
    brief_id = Column(Integer, ForeignKey("briefs.id"))
    intent_text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    brief = relationship("Brief", back_populates="intents")

class Query(Base):
    __tablename__ = "queries"
    id = Column(Integer, primary_key=True, index=True)
    brief_id = Column(Integer, ForeignKey("briefs.id"))
    query_text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    brief = relationship("Brief", back_populates="queries")
    evidence = relationship("Evidence", back_populates="query")

class Evidence(Base):
    __tablename__ = "evidence"
    id = Column(Integer, primary_key=True, index=True)
    query_id = Column(Integer, ForeignKey("queries.id"))
    content = Column(Text, nullable=False)
    source = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    query = relationship("Query", back_populates="evidence")