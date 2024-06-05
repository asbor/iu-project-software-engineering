from pydantic import BaseModel


class SugarBase(BaseModel):
    """
    Sugar model

    Attributes:
        id : The unique identifier for the sugar.

    Relationships:
        fermentable_id : The fermentable relationship.
    """

    total_ibu_per_kg: float
