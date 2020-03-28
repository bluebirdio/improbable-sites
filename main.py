from fastapi import FastAPI, APIRouter
from fastapi_sqlalchemy import DBSessionMiddleware
from api.settings import *
from api.users.api import router as users
from api.roles.api import router as roles
from api.teams.api import router as teams
from api.stacks.api import router as stacks
from api.apps.api import router as apps
from api.environments.api import router as environments
from api.repositories.api import router as repositories
from api.instances.api import router as instances
from api.apps_instances.api import router as apps_instances
import uvicorn


api = FastAPI()

api.title = 'Sites API'
api.openapi_url = "/v1/openapi.json"

api.add_middleware(DBSessionMiddleware, db_url=DATABASE_URL)

# Allow each module to define its own routes separately and include them here with namespaces.
router = APIRouter()
router.include_router(apps, prefix="/apps", tags=["Apps"])
router.include_router(apps_instances, prefix="/apps", tags=["Apps"])
router.include_router(instances, prefix="/instances", tags=["Apps"])
router.include_router(environments, prefix="/environments", tags=["Apps"])
router.include_router(stacks, prefix="/stacks", tags=["Stacks"])
router.include_router(users, prefix="/users", tags=["Users and teams"])
router.include_router(roles, prefix="/roles", tags=["Users and teams"])
router.include_router(teams, prefix="/teams", tags=["Users and teams"])
router.include_router(repositories, prefix="/repositories", tags=["Repositories"])

api.include_router(router, prefix="/v1")

if __name__ == "__main__":
    uvicorn.run(api, host=LISTEN_HOST, port=LISTEN_PORT)