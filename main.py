from fastapi import FastAPI
import uvicorn

api = FastAPI()

api.title = 'Sites'
api.openapi_url = "/v1/openapi.json"


@api.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run(api, host="0.0.0.0", port=8000)