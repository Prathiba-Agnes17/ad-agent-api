from fastapi import FastAPI
from pydantic import BaseModel
from ad_tools import change_password, reset_password, lock_account, unlock_account
 
app = FastAPI()
 
class ActionRequest(BaseModel):
    username: str
 
@app.post("/change_password")
def change_password_endpoint(request: ActionRequest):
    return {"result": change_password({"username": request.username})}
 
@app.post("/reset_password")
def reset_password_endpoint(request: ActionRequest):
    return {"result": reset_password({"username": request.username})}
 
@app.post("/lock_account")
def lock_account_endpoint(request: ActionRequest):
    return {"result": lock_account({"username": request.username})}
 
@app.post("/unlock_account")
def unlock_account_endpoint(request: ActionRequest):
    return {"result": unlock_account({"username": request.username})}
 
