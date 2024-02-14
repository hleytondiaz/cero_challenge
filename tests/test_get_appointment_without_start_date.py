from config import config
from utils import get_future_date
import requests

"""
    This test verifies that a medical appointment cannot be retrieved due to an undefined start date.
"""

def test_get_appointment():
    url = config["LOCALHOST"] + "/citas"

    headers = {
        "x-api-key": config['API_KEY']
    }

    id_branch = 1
    end_date = get_future_date()
    
    params = {
        "id_branch": id_branch,
        "end_date": end_date
    }
        
    response = requests.get(url, headers=headers, params=params)

    assert response.status_code == 422