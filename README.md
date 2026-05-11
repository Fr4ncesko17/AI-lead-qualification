# AI Lead Qualification Engine

AI-powered lead qualification backend built with FastAPI, Gemini and SQLite.

## Features

- AI lead scoring
- Lead classification
- Recommendation engine
- FastAPI backend
- Swagger documentation
- SQLite persistence
- JSON validation with Pydantic

---

## Tech Stack

- Python
- FastAPI
- Gemini API
- SQLite
- Pydantic

---

## Installation

```bash
git clone <repo_url>

cd ai-lead-engine

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key
```

---

## Run API

```bash
uvicorn app.main:app --reload
```

---

## Swagger Docs

```text
http://127.0.0.1:8000/docs
```

---

## Endpoints

### POST `/evaluate`

Evaluates and stores lead information.

### GET `/leads`

Returns lead history.

---

## Example Request

```json
{
  "name": "Juan Kapo",
  "company": "TechCorp",
  "role": "CTO",
  "company_size": 80,
  "need": "Implementar soluciones de ciberseguridad",
  "budget": "alto",
  "urgency": "alta"
}
```

---

## Future Improvements

- PostgreSQL
- Docker
- Authentication
- CRM integrations
- Frontend dashboard