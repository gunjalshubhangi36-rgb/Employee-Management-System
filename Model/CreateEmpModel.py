from pydantic import BaseModel, Field
from typing import Annotated

class EmpStruct(BaseModel):
    Id : Annotated[int , Field(title="Enter your Id")]
    Name : Annotated[str, Field(title="Enter your name")]
    Dept : Annotated[str, Field(title="Enter your department")]
    Sallary : Annotated[int, Field(title="Enter your sallary")]


