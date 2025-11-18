import requests
import src.config as cfg

def build_radar_url():
    """based on config conduct radar URL"""

    north = cfg.CENTER_LAT + cfg.LAT_OFFSET
    south = cfg.CENTER_LAT - cfg.LAT_OFFSET
    east  = cfg.CENTER_LON + cfg.LON_OFFSET
    west  = cfg.CENTER_LON - cfg.LON_OFFSET

    url = (
        "https://v6.bvg.transport.rest/radar"
        f"?north={north:.6f}"
        f"&west={west:.6f}"
        f"&south={south:.6f}"
        f"&east={east:.6f}"
        f"&results={cfg.RESULTS}"
        f"&duration={cfg.DURATION}"
        f"&frames={cfg.FRAMES}"
    )
    return url


def fetch_radar_data():
    """ send radar API request and return as json"""
    url = build_radar_url()
    r = requests.get(url, timeout=10)
    return r.json()
