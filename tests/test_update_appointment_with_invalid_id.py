from config import config
import requests

"""
    This test allows verifying that a medical appointment cannot be updated due to an invalid ID.
"""

def test_update_appointment():
    id_appointment = 12345678
    id_status = 16

    url = config["LOCALHOST"] + "/citas/" + str(id_appointment)

    headers = {
        "x-api-key": config['API_KEY']
    }

    data = {
        "id_status": id_status
    }

    response = requests.put(url, json=data, headers=headers)

    message = response.json()["error"]["message"]

    assert response.status_code == 200 and message == "No existe cita con ese ID"