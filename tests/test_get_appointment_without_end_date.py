from config import config
from utils import get_current_date
import requests

"""
    This test verifies that a medical appointment cannot be retrieved due to an undefined end date.
"""

def test_get_appointment():
    url = config["LOCALHOST"] + "/citas"

    headers = {
        "x-api-key": config['API_KEY']
    }

    id_branch = 1
    start_date = get_current_date()
    
    params = {
        "id_branch": id_branch,
        "start_date": start_date
    }
        
    response = requests.get(url, headers=headers, params=params)

    assert response.status_code == 422