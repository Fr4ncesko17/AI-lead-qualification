import sqlite3
from datetime import datetime

DB_PATH = "data/leads.db"

def init_db():

    print("🔥 Initializing database...")

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS leads (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        company TEXT,
        role TEXT,
        company_size INTEGER,
        need TEXT,
        budget TEXT,
        urgency TEXT,
        score INTEGER,
        classification TEXT,
        action TEXT,
        reason TEXT,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()
    print("✅ Database initialized")


def save_lead(lead_data, evaluation):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO leads (
        name,
        company,
        role,
        company_size,
        need,
        budget,
        urgency,
        score,
        classification,
        action,
        reason,
        created_at
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        lead_data["name"],
        lead_data["company"],
        lead_data["role"],
        lead_data["company_size"],
        lead_data["need"],
        lead_data["budget"],
        lead_data["urgency"],
        evaluation["score"],
        evaluation["classification"],
        evaluation["action"],
        evaluation["reason"],
        datetime.now().isoformat()
    ))

    conn.commit()
    print("✅ Lead saved to database")
    conn.close()
    
def get_all_leads():

    conn = sqlite3.connect(DB_PATH)

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM leads
    ORDER BY created_at DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]