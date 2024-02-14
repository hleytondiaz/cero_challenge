from config import config
import requests

def test_update_appointment():
    id_appointment = 328
    id_status = 250

    url = config["LOCALHOST"] + "/citas/" + str(id_appointment)

    headers = {
        "x-api-key": config['API_KEY']
    }

    data = {
        "id_status": id_status
    }

    response = requests.put(url, json=data, headers=headers)

    message = response.json()["error"]["message"]

    assert response.status_code == 200 and message == "Estado no existe o se encuentra deshabilitado"