from pydantic import BaseModel


class LiquidExtractBase(BaseModel):
    """Liquid Extract model.

    Attributes:
        id : The unique identifier for the liquid extract.

    Relationships:
        fermentable_id : The fermentable relationship.
    """

    total_ibu_per_kg: float
