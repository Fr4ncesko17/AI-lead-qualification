import os
import json
from google import genai

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def evaluate_lead(lead_data: dict):

    prompt = f"""
You are a senior B2B sales analyst specialized in lead qualification.

Your task is to evaluate the quality of a lead based on:
- Company size
- Role
- Need
- Budget
- Urgency
- Fit

Instructions:
1. Assign a score from 0 to 100
2. Classify:
   0–30 → Low
   31–60 → Medium
   61–100 → High
3. Recommend action:
   Low → Descartado
   Medium → Interesado
   High → Calificado or Enviar propuesta
4. Provide a concise reason

Rules:
- Do not invent data
- Return ONLY valid JSON

Output:
{{
  "score": number,
  "classification": "Low | Medium | High",
  "action": "Descartado | Interesado | Calificado | Enviar propuesta",
  "reason": "string"
}}

Lead:
{lead_data}
"""

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    raw_text = response.text

    try:
        parsed = json.loads(raw_text)

        required_keys = ["score", "classification", "action", "reason"]

        for key in required_keys:
            if key not in parsed:
                raise ValueError(f"Missing key: {key}")

        if not isinstance(parsed["score"], (int, float)):
            raise ValueError("Score must be a number")

        parsed["classification"] = parsed["classification"].capitalize()
        parsed["action"] = parsed["action"].capitalize()

        return parsed

    except Exception as e:
        return {
            "error": "Invalid response from model",
            "raw_response": raw_text,
            "details": str(e)
        }