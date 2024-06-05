from pydantic import BaseModel


class User(BaseModel):
    """
Description:

This class represents the user table in the database.

Use cases:

- Validate data before entering it into the database.

Notes:

- the id field is optional because it is generated by the database.

    """

    username: str
    password: str
