from pydantic import BaseModel
from datetime import datetime


class FermentableCreate(BaseModel):
    """
    Fermentable creation schema

    Attributes:
          name (str): The name of the fermentable.
          amount (int): The amount of the fermentable in kilograms.
          cost per unit (EUR): The cost per unit in Euros.
          supplier (str): The supplier of the fermentable.
          origin (str): The origin of the fermentable.
          type (str): The type of the fermentable.
          color (int): The color of the fermentable in EBC.
          potential (int): The potential of the fermentable in PPG (Points Per Gallon).
          yield (%): The yield of the fermentable as a percentage.
          manufacturing Date: The manufacturing date of the fermentable.
          expiry Date: The expiry date of the fermentable.
          lot Number (str): The lot number of the fermentable.
          exclude from total (bool): Indicates whether to exclude the fermentable from the total.
          not fermentable (bool): Indicates whether the fermentable is not fermentable.
          notes (str): Additional notes about the fermentable.
          description (str): Description of the fermentable.
          substitutes (str): Substitutes for the fermentable.
          used in (str): Where the fermentable is used.
    """
    name: str
    amount: int
    cost_per_unit: float
    supplier: str
    origin: str
    type: str
    color: int
    potential: int
    yield_: float
    manufacturing_date: datetime
    expiry_date: datetime
    lot_number: str
    exclude_from_total: bool
    not_fermentable: bool
    notes: str
    description: str
    substitutes: str
    used_in: str
