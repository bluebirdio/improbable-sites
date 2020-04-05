import uvicorn
from fastapi import APIRouter, FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from sqlalchemy import create_engine

from api.applications.api import router as applications
from api.instances.api import router as instances
from api.repositories.api import router as repositories
from api.roles.api import router as roles
from api.settings import *
from api.stacks.api import router as stacks
from api.teams.api import router as teams
from api.users.api import router as users

api = FastAPI()

api.title = "Sites API"
api.openapi_url = "/v1/openapi.json"

db_engine = create_engine(DATABASE_URL, connect_args=DATABASE_ARGS)
api.add_middleware(DBSessionMiddleware, custom_engine=db_engine)


# Allow each module to define its own routes separately and include them here with namespaces.
router = APIRouter()
router.include_router(applications, prefix="/applications", tags=["Applications"])
router.include_router(instances, prefix="/instances", tags=["Applications"])
router.include_router(stacks, prefix="/stacks", tags=["Stacks"])
router.include_router(users, prefix="/users", tags=["Users and teams"])
router.include_router(roles, prefix="/roles", tags=["Users and teams"])
router.include_router(teams, prefix="/teams", tags=["Users and teams"])
router.include_router(repositories, prefix="/repositories", tags=["Repositories"])

api.include_router(router, prefix="/v1")


@api.get("/", response_model=list)
async def root():
    return [
        {
            "version": "1.0",
            "name": "Original version",
            "url": "/v1"
        }
    ]


if __name__ == "__main__":
    uvicorn.run(api, host=LISTEN_HOST, port=LISTEN_PORT)
