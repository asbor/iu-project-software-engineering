import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from ...base import Base


class Grain(Base):
    """
    Grain model

    Attributes:
        id (UUID): The unique identifier for the grain.
        diastatic_power (decimal): The diastatic power of the grain.
        moisture (decimal): The moisture content of the grain.
        protein (decimal): The protein content of the grain.
        coarse_fine_diff (decimal): The coarse fine difference of the grain.
        extract (decimal): The extract of the grain.
        acidity (decimal): The acidity of the grain.
        friability (decimal): The friability of the grain.
        free_amino_nitrogen (decimal): The free amino nitrogen of the grain.
        max_in_batch (decimal): The maximum amount of the grain in the batch.

    Relationships:
        fermentable_id (uuid): The fermentable relationship.
    """

    __tablename__ = "grain"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    diastatic_power = Column(Float, nullable=False)
    moisture = Column(Float, nullable=False)
    protein = Column(Float, nullable=False)
    coarse_fine_diff = Column(Float, nullable=False)
    extract = Column(Float, nullable=False)
    acidity = Column(Float, nullable=False)
    friability = Column(Float, nullable=False)
    free_amino_nitrogen = Column(Float, nullable=False)
    max_in_batch = Column(Float, nullable=False)

    # Relationships for the fermentable types 1:1
    fermentable_id = Column(UUID, ForeignKey("fermentable.id"))
    fermentable = relationship(
        "Fermentable", uselist=False, back_populates="grain")

    def __repr__(self):
        return f"<Grain {self.id}, \
                diastatic_power={self.diastatic_power}, \
                moisture={self.moisture}, \
                protein={self.protein}, \
                coarse_fine_diff={self.coarse_fine_diff}, \
                extract={self.extract}, \
                acidity={self.acidity}, \
                friability={self.friability}, \
                free_amino_nitrogen={self.free_amino_nitrogen}, \
                max_in_batch={self.max_in_batch}>"
