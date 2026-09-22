from pymongo import MongoClient


ConnectionString = MongoClient("mongodb+srv://Shubhangi:MlWyCgPRM2PLguLo@test.0ro6rrk.mongodb.net/?appName=test")

database = ConnectionString["Emp_Db"]

emp_collection = database["Emp_Collection"]



