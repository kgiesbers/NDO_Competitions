from fastapi import FastAPI
from API.routes.competition_by_competitor import router

app = FastAPI()
app.include_router(router)
