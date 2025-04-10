from fastapi import APIRouter
from data_access.database.database_interactors.database_queries.competition_by_competitor import competition_by_competitor


router = APIRouter()


@router.get("/competition_by_competitor/{competitor_name}")
def read_competition_by_competitor(competitor_name: str):
    return competition_by_competitor(competitor_name)
