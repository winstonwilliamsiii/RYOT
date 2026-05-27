#FastAPI Scaffold
#main python file to run the API

from fastapi import FastAPI
from api.reparations.routes import router as reparations_router
from api.civic_data.routes import router as civic_router
from api.complaints.routes import router as complaints_router

app = FastAPI(title="RYOT Civic Platform")

# Register routers
app.include_router(reparations_router, prefix="/reparations", tags=["Reparations"])
app.include_router(civic_router, prefix="/civic", tags=["Civic Data"])
app.include_router(complaints_router, prefix="/complaints", tags=["Complaints"])

@app.get("/")
def root():
    return {"status": "ok", "message": "RYOT API running"}
