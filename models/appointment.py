from pydantic import BaseModel

"""
    This file contains the model for an appointment to be used in the update process.
"""

class Appointment(BaseModel):
    id_status: int