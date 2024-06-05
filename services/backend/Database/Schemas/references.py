from pydantic import BaseModel

from typing import Optional

from datetime import datetime





class ReferenceBase(BaseModel):

    name: str

    url: str

    description: Optional[str] = None

    category: Optional[str] = None

    favicon_url: Optional[str] = None





class ReferenceCreate(ReferenceBase):

    pass





class ReferenceUpdate(ReferenceBase):

    pass





class ReferenceInDBBase(ReferenceBase):

    id: int

    created_at: datetime

    updated_at: Optional[datetime] = None



    class Config:

        from_attributes = True





class Reference(ReferenceInDBBase):

    pass
