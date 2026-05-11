from pydantic import BaseModel

class LeadRequest(BaseModel):
    name: str
    company: str
    role: str
    company_size: int
    need: str
    budget: str
    urgency: str