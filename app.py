from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers import appointments

app = FastAPI()

@app.get("/")
def docs_redirect():
    return RedirectResponse(url="/docs")

app.include_router(appointments.router)