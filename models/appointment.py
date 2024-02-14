from pydantic import BaseModel
from datetime import date

class Appointment(BaseModel):
    id_status: int