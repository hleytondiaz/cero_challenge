from config import config
import requests

"""
    This test allows verifying that a medical appointment cannot be updated due to an invalid status.
"""

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

    condition_1 = message == "Estado no existe o se encuentra deshabilitado"
    condition_2 = message == "La cita que está intentando modificar está anulada"

    assert response.status_code == 200 and (condition_1 or condition_2)