from pydantic import BaseModel, Field
from typing import Annotated, Optional

class UpdateStruct(BaseModel):
    Name : Annotated[Optional[str], Field(title="Enter your name", default=None)] 
    Dept : Annotated[Optional[str], Field(title="Enter your department", default=None)]
    Sallary : Annotated[Optional[int], Field(title="Enter your sallary",default=None)]