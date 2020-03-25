from fastapi import APIRouter

from .models import *
from . import tables

from api.core.db_crud import *
from typing import List

router = APIRouter()


@router.get("/", response_model=List[Team], response_description="Return a list of teams")
def list_teams():
    return query(tables.Team)


@router.post("/", response_model=Team, response_description="Create a new team.")
def create_team(team_in: Team):
    return create(tables.Team, team_in)


@router.get("/{id}", response_model=Team)
def get_team(id: str):
    return get_or_error(tables.Team, id, "Team not found")


@router.put("/{id}", response_model=Team)
def update_team(*, id: str, team_in: Team):
    return update(tables.Team, id, team_in)


@router.delete("/{id}", response_model=Team)
def delete_team(id: str):
    return delete(tables.Team, id)

