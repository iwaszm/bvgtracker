# src/save_csv.py

import csv
import os
from datetime import datetime
import src.config as cfg

def init_csv():
    """initial CSV if not exists"""
    folder = os.path.dirname(cfg.CSV_FILE)
    os.makedirs(folder, exist_ok=True)

    if not os.path.exists(cfg.CSV_FILE):
        with open(cfg.CSV_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "timestamp",
                "tripId",
                "line",
                "direction",
                "latitude",
                "longitude",
                "heading",
                "speed"
            ])

def append_rows(rows):
    """write in CSV"""
    with open(cfg.CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        now = datetime.utcnow().isoformat()

        for r in rows:
            writer.writerow([
                now,
                r["tripId"],
                r["line"],
                r["direction"],
                r["lat"],
                r["lon"],
                r["heading"],
                r["speed"]
            ])
