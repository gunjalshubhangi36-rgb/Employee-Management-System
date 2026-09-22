from fastapi import FastAPI

from Routes.EmpRoutes import router

app = FastAPI(title="Employ management system API")

app.include_router(router)

@app.get("/")
def Welcome():
    return {"message":"Welcome to employee management system"}

