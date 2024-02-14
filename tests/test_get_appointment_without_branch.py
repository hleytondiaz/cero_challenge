from config import config
from utils import get_current_date, get_future_date
import requests

def test_get_appointment():
    url = config["LOCALHOST"] + "/citas"

    headers = {
        "x-api-key": config['API_KEY']
    }

    start_date = get_current_date()
    end_date = get_future_date()
    
    params = {
        "start_date": start_date,
        "end_date": end_date
    }
        
    response = requests.get(url, headers=headers, params=params)

    assert response.status_code == 422