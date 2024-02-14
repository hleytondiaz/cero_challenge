from config import config
import requests

def test_update_appointment():
    id_appointment = 328
    id_status = 16

    url = config["LOCALHOST"] + "/citas/" + str(id_appointment)

    headers = {
        "x-api-key": config['API_KEY']
    }

    data = {
        "id_status": id_status
    }

    response = requests.put(url, json=data, headers=headers)

    assert response.status_code == 200