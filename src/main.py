from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.engine_session.database import Base, engine
from src.api import main_router
from starlette import status
from starlette.exceptions import HTTPException

app = FastAPI()
app.include_router(main_router)

@asynccontextmanager
async def lifespan():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
            yield
            await conn.commit()
            await conn.dispose()
    except:
        raise (HTTPException(status_code=404, detail='error'))




