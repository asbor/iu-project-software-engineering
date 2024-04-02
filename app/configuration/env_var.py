from pydantic import BaseSettings

# Environment variables are processed using the
# [BaseSettings](https://docs.pydantic.dev/usage/settings/) object of the [pydantic](https://docs.pydantic.dev/) library.


class Settings(BaseSettings):
    redis_host = 'localhost'

    class Config:
        case_sensitive = True

    NAME: str


settings = Settings()
