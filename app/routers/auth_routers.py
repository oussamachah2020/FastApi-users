import uuid

from fastapi_users import FastAPIUsers

from auth_utils.managers import User, get_user_manager
from auth_utils.backends import auth_backend

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)
