from pydantic import BaseModel





class AdjunctBase(BaseModel):

    """

    Adjunct model


    Attributes:

        id : The unique identifier for the adjunct.

        total_ibu_per_kg (float): The total IBU per kg of the adjunct.

    Relationships:

        fermentable (Fermentable): The associated fermentable.

    """



    total_ibu_per_kg: float
