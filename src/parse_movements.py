
import src.config as cfg

def extract_bus_movements(data):
    """filter the target from radar data"""

    movements = data.get("movements", [])
    results = []

    for m in movements:
        line = m.get("line", {})
        if line.get("product") != cfg.LINE_PRODUCT:
            continue
        if line.get("name") != cfg.LINE_NAME:
            continue

        loc = m.get("location", {})

        results.append({
            "tripId": m.get("tripId"),
            "line": line.get("name"),
            "direction": m.get("direction"),
            "lat": loc.get("latitude"),
            "lon": loc.get("longitude"),
            "heading": m.get("heading"),
            "speed": m.get("speed")
        })

    return results
