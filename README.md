# Briefs API

FastAPI-based REST API for managing briefs, intents, queries, and evidence.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

3. Visit http://127.0.0.1:8000/docs for interactive API documentation.

## Project Structure

```
app/
├── __init__.py
├── main.py          # FastAPI app entry point
├── models.py        # SQLAlchemy models
├── schemas.py       # Pydantic schemas
├── database.py      # Database setup
└── routers/
    ├── __init__.py
    ├── briefs.py
    ├── evidence.py
    ├── intents.py
    └── queries.py
```

## Endpoints

- **Briefs**: `/briefs`
- **Intents**: `/intents`
- **Queries**: `/queries`
- **Evidence**: `/evidence`