from contextlib import asynccontextmanager
from fastapi import FastAPI

from database import create_tables, delete_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('base remove')
    await create_tables()
    print("base ready!")
    yield
    print('Выключение111!')

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)







