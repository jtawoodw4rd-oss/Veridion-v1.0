# Veridion v1.0

A FastAPI-based REST API for managing briefs, intents, queries, and evidence.

## Features
- Create and manage briefs
- Add intents, queries, and evidence to briefs
- SQLite database for persistence
- Interactive API documentation

## API Endpoints
- `GET /` - Root endpoint
- `POST /briefs/` - Create a brief
- `GET /briefs/` - Get all briefs
- `GET /briefs/{brief_id}` - Get a specific brief
- `DELETE /briefs/{brief_id}` - Delete a brief
- And more for intents, queries, and evidence

## Documentation
- Swagger UI: `/docs`
- ReDoc: `/redoc`
