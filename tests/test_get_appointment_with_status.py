from config import config
from utils import get_current_date, get_future_date
import requests

def test_get_appointment():
    url = config["LOCALHOST"] + "/citas"

    headers = {
        "x-api-key": config['API_KEY']
    }

    id_branch = 1
    start_date = get_current_date()
    end_date = get_future_date()
    id_status = 26
    
    params = {
        "id_branch": id_branch,
        "start_date": start_date,
        "end_date": end_date,
        "id_status": id_status
    }
        
    response = requests.get(url, headers=headers, params=params)

    assert response.status_code == 200