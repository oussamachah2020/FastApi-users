import uuid
from auth_utils.misc import create_user
from models.auth_models import create_db_and_tables
from schemas.auth_schemas import UserRead, UserCreate
from auth_utils.managers import User, get_user_manager
from auth_utils.backends import auth_backend
from fastapi_users import FastAPIUsers
from fastapi import FastAPI
import asyncio

app = FastAPI()

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)


app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


@app.on_event("startup")
async def startup():
    try:
        await create_db_and_tables()
        await create_user("king.arthur@camelot.bt", "guinevere")
    except Exception as e:
        print(f"Error on startup: {e}")
