from Model.CreateEmpModel import EmpStruct
from Model.UpdateEmpModel import UpdateStruct
from Database.Connection import emp_collection

def get_Emp():
    all_data = list(emp_collection.find({},{"_id": 0 }))
    return all_data

def post_Emp(emp : EmpStruct):
    sid = emp.Id
    sname = emp.Name
    sdept = emp.Dept
    ssallary = emp.Sallary

    sdict = {
        "Id" : sid,
        "Name" : sname,
        "Dept" : sdept,
        "Sallary": ssallary
    }
    emp_collection.insert_one(sdict)

    return {"message":"Employee Created"}

def UpdateModel(Id : int, emp_update : UpdateStruct):
    allData = list(emp_collection.find({},{"_id" : 0}))

    UpdateEmp = {}

    for i in allData:

        if i["Id"] == Id:

            if emp_update.Name != None:
                UpdateEmp["Name"] = emp_update.Name

            if emp_update.Dept != None:
                UpdateEmp["Dept"] = emp_update.Dept

            if emp_update.Sallary != None:
                UpdateEmp["Sallary"] = emp_update.Sallary

            emp_collection.update_one(
                {"Id": Id},
                {"$set":UpdateEmp}
            )

            return {"message":"student Updated"}

def DeleteModel(Id:int):
    allData = list(emp_collection.find({},{"_id" :0}))

    for i in allData:

        if i["Id"] == Id:

            emp_collection.delete_one({"Id":Id})
            return {"message":"Employee deleted"}




        




