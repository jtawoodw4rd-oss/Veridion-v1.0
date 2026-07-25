from fastapi import FastAPI
from app.routers import briefs, evidence, intents, queries

app = FastAPI(title="Briefs API")

app.include_router(briefs.router, prefix="/briefs", tags=["briefs"])
app.include_router(evidence.router, prefix="/evidence", tags=["evidence"])
app.include_router(intents.router, prefix="/intents", tags=["intents"])
app.include_router(queries.router, prefix="/queries", tags=["queries"])

@app.get("/")
def root():
    return {"message": "Briefs API is running"}