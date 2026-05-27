#FastAPI Scaffold
#routes

from fastapi import APIRouter

router = APIRouter()

# Example: running tally endpoint
@router.get("/counter")
def get_reparations_counter():
    # Placeholder: load from dataset or DB
    tally = {"amount_owed": 14_000_000_000_000, "currency": "USD"}
    return tally
