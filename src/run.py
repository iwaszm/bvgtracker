# src/run.py

import time
from datetime import datetime

import src.config as cfg
from src.fetch_radar import fetch_radar_data
from src.parse_movements import extract_bus_movements
from src.save_csv import init_csv, append_rows

def main():
    init_csv()
    print("🚍 Start tracking Bus", cfg.LINE_NAME)
    print("Saving to:", cfg.CSV_FILE)

    while True:
        try:
            data = fetch_radar_data()
            buses = extract_bus_movements(data)

            if buses:
                append_rows(buses)
                print(f"[{datetime.utcnow().isoformat()}] Saved {len(buses)} points")
            else:
                print(f"[{datetime.utcnow().isoformat()}] No bus found")

        except Exception as e:
            print("⚠ Error:", e)

        time.sleep(cfg.INTERVAL)


if __name__ == "__main__":
    main()
