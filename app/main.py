from fastapi import FastAPI
from app.lead_service import evaluate_lead
from app.models import LeadRequest
from app.database import init_db, save_lead, get_all_leads
app = FastAPI()

init_db()

@app.get("/")
def root():
    return {"message": "AI Lead Qualification Engine running"}

@app.post("/evaluate")
def evaluate(data: LeadRequest):

    lead_data = data.dict()

    result = evaluate_lead(lead_data)

    if "error" not in result:
        save_lead(lead_data, result)

    return result

@app.get("/leads")
def get_leads():

    return get_all_leads()