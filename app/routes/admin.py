# admin.py – route handlers for Admin APIs
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from bson import ObjectId
from .. import models
from ..auth import require_admin
from ..db import db

router = APIRouter()  # Create router instance

@router.get("/plans")
async def list_plans(current_user = Depends(require_admin)):
    plans_cursor = db["plans"].find()
    plans = await plans_cursor.to_list(length=100)
    for plan in plans:
        plan.pop("_id", None)
    return plans

@router.post("/plans")
async def create_plan(plan: models.SubscriptionPlan, current_user = Depends(require_admin)):
    existing = await db["plans"].find_one({"name": plan.name})
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="A plan with this name already exists")
    plan_doc = plan.dict()
    result = await db["plans"].insert_one(plan_doc)
    return {"detail": f"Plan '{plan.name}' created successfully", "plan_id": str(result.inserted_id)}

@router.put("/plans/{plan_name}")
async def update_plan(plan_name: str, plan: models.SubscriptionPlan, current_user = Depends(require_admin)):
    # Update an existing plan's quotas (name cannot be changed)
    if plan.name != plan_name:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Plan name mismatch")
    plan_data = plan.dict()
    plan_data.pop("name", None)
    result = await db["plans"].update_one({"name": plan_name}, {"$set": plan_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Plan not found")
    return {"detail": f"Plan '{plan_name}' updated successfully"}

@router.delete("/plans/{plan_name}")
async def delete_plan(plan_name: str, current_user = Depends(require_admin)):
    result = await db["plans"].delete_one({"name": plan_name})
    if result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Plan not found")
    return {"detail": f"Plan '{plan_name}' has been deleted"}

@router.get("/users", response_model=List[models.UserOut])
async def list_users(current_user = Depends(require_admin)):
    users_cursor = db["users"].find()
    users = await users_cursor.to_list(length=100)
    users_out = []
    for user in users:
        user["id"] = str(user["_id"])
        user.pop("_id", None)
        users_out.append(user)
    return users_out

@router.post("/users", response_model=models.UserOut)
async def create_user(user: models.UserCreate, current_user = Depends(require_admin)):
    # If a plan name is provided, ensure it exists
    plan_name = user.plan
    if plan_name:
        plan_doc = await db["plans"].find_one({"name": plan_name})
        if not plan_doc:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid plan name")
    # Generate a new API key for the user
    import secrets
    api_key = secrets.token_urlsafe(32)
    # Prepare the user document
    zero_usage = {f"service{i}": 0 for i in range(1, 7)}
    user_doc = {
        "name": user.name,
        "role": "customer",
        "api_key": api_key,
        "plan": plan_name,
        "usage": zero_usage
    }
    result = await db["users"].insert_one(user_doc)
    user_doc["id"] = str(result.inserted_id)
    user_doc.pop("_id", None)
    return user_doc

@router.put("/users/{user_id}")
async def change_user_plan(user_id: str, plan: models.PlanAssign, current_user = Depends(require_admin)):
    try:
        obj_id = ObjectId(user_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid user ID")
    plan_doc = await db["plans"].find_one({"name": plan.plan})
    if not plan_doc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Plan not found")
    zero_usage = {f"service{i}": 0 for i in range(1, 7)}
    result = await db["users"].update_one({"_id": obj_id}, {"$set": {"plan": plan.plan, "usage": zero_usage}})
    if result.matched_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return {"detail": f"Plan '{plan.plan}' assigned to user {user_id}"}

