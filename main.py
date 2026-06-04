from contextlib import asynccontextmanager
from fastapi import FastAPI,Request
from scalar_fastapi import get_scalar_api_reference
from route.task_route import router as task_router
from route.admin_route import router as admin_router
import time
from database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Welcome to lifespan")
    await init_db()

    yield
    print("Bye from lifespan")

app = FastAPI(
    title='Task API',
    description='This Documentation provide task Api for learning',
    version='0.0',
    lifespan=lifespan
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    s=time.perf_counter()
    response = await call_next(request)
    e=time.perf_counter()
    print(e-s)
    return response


@app.get("/scalar", include_in_schema=False)
def scalar():

    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )

app.include_router(task_router,prefix="/task",tags=["task"])
app.include_router(admin_router,prefix="/admin",tags=["admin"])