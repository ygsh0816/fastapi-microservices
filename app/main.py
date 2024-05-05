from fastapi import FastAPI, status
import app.models as models
from app.database import engine
from app.routers import auth, todos
from starlette.staticfiles import StaticFiles, RedirectResponse

fast_app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@fast_app.get("/")
async def home():
    # return {"default": "Welcome finally"}
    return RedirectResponse("/auth", status_code=status.HTTP_302_FOUND)

fast_app.mount("/static", StaticFiles(directory="app/static"), name="static")

fast_app.include_router(auth.router)
fast_app.include_router(todos.router)
