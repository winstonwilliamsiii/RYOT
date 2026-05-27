#FastAPI Routes for civic_data

from fastapi import APIRouter

router = APIRouter()

@router.get("/votes/{bill_id}")
def get_vote_tally(bill_id: str):
    # Placeholder: integrate with Congress.gov / OpenStates API
    return {
        "bill_id": bill_id,
        "yea": 220,
        "nay": 210,
        "abstain": 5
    }

@router.get("/politicians")
def list_politicians():
    # Placeholder: static dataset or API call
    return [
        {"name": "Jane Doe", "role": "Senator", "contact": "jane.doe@senate.gov"},
        {"name": "John Smith", "role": "Representative", "contact": "john.smith@house.gov"}
    ]
