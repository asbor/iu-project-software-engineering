from pydantic import BaseModel


class GrainBase(BaseModel):
    """
    Grain model

    Attributes:
        id : The unique identifier for the grain.
        diastatic_power (float): The diastatic power of the grain.
        moisture (float): The moisture content of the grain.
        protein (float): The protein content of the grain.
        coarse_fine_diff (float): The coarse fine difference of the grain.
        extract (float): The extract of the grain.
        acidity (float): The acidity of the grain.
        friability (float): The friability of the grain.
        free_amino_nitrogen (float): The free amino nitrogen of the grain.
        max_in_batch (float): The maximum amount of the grain in the batch.
        fermentable_id : The ID of the associated fermentable.

    Relationships:
        fermentable (Fermentable): The associated fermentable.
    """

    diastatic_power: float
    moisture: float
    protein: float
    coarse_fine_diff: float
    extract: float
    acidity: float
    friability: float
    free_amino_nitrogen: float
    max_in_batch: float
