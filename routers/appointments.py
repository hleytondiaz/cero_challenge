from fastapi import APIRouter, HTTPException, Depends
from config import config
from datetime import date
from models.appointment import Appointment
from middlewares import verify_key
import requests
import json

"""
    This file contains the logic necessary to retrieve medical appointments and update a specific one through its ID.
"""

router = APIRouter(prefix="/citas")

@router.get("/", dependencies=[Depends(verify_key)])
def get_appointments(id_branch: int, start_date: date, end_date: date, id_status: int = None):
    try:
        url = config["API_HOST"] + "/citas"
        
        headers = {
            "Authorization": "Token " + config['TOKEN']
        }
        
        query_parameters = {
            "id_sucursal": {"eq": id_branch},
            "fecha": [{"gte": str(start_date)}, {"lte": str(end_date)}],
        }
        
        if id_status != None:
            query_parameters["id_estado"] = {"eq": id_status}

        query_string = "?q=" + json.dumps(query_parameters)
        
        response = requests.get(url + query_string, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail="Error querying the Dentalink API")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error: " + str(e))
    
@router.put("/{id_appointment}", dependencies=[Depends(verify_key)])
def update_appointment(id_appointment: int, appointment: Appointment):
    try:
        url = config["API_HOST"] + "/citas/" + str(id_appointment)

        headers = {
            "Authorization": "Token " + config['TOKEN']
        }

        data = {
            "id_estado": appointment.id_status
        }

        response = requests.put(url, json=data, headers=headers)
        
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error: " + str(e))