from fastapi import APIRouter
from Controller.EmpController import(
    get_Emp,
    post_Emp,
    UpdateModel,
    DeleteModel
)
from Database.Connection import emp_collection
from Model.CreateEmpModel import EmpStruct
from Model.UpdateEmpModel import UpdateStruct   

router = APIRouter()

@router.get("/alldata")
def get_all_emp():
    return get_Emp()

@router.post("/add_emp")
def post_data(emp: EmpStruct):
    return post_Emp(emp)

@router.put("/edit_emp/{Id}")
def Update_Emp(Id : int, emp_update : UpdateStruct):
    return UpdateModel(Id, emp_update)

@router.delete("/delete_emp/{Id}")
def Update_Emp(Id : int):
    return DeleteModel(Id)