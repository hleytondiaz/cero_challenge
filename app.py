from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers import appointments

"""
    This file has the purpose of initializing the application with FastAPI. By default, the root route redirects to the API documentation. Additionally, the rest of the routes are handled externally.
"""

app = FastAPI()

@app.get("/")
def docs_redirect():
    return RedirectResponse(url="/docs")

app.include_router(appointments.router)