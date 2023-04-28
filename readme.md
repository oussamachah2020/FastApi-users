# This is a guide that helps create this API project

### Inside your project folder create a virtual environment by executing this command

```bash
python -m venv .venv
```

or

```bash
python3 -m venv .venv
```

### Then activate it by running the following command

> for fish terminal:

```fish
source .venv/bin/activate.fish
```

### To Create a requirements file that contains all dependencies

### run this command

```bash
pip freeze > requirements.txt
```

> you have to create an `app/` folder where all your api will be created

### To use the environment variables

### create `config/settings.py` and write the following code

```python
from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_HOSTNAME: str

    class Config:
        env_file: "path/to/env/file"


settings = Settings()

```

> The Settings class inherits from `BaseSettings`, inside it you type your variables and then create an instance for the `Settings` class so you can import it and use it

### Depending on the transporter you are using, you create a `auth_utils/backends.py`

> In this case, we are using JWT transporter

```python
from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy
from config.settings import settings

SECRET = settings.JWT_PRIVATE_KEY

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

```
