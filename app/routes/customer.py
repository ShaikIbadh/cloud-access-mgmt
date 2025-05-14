from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from .. import models
from ..auth import require_customer
from ..db import db

router = APIRouter()

@router.get("/plans", response_model=List[models.SubscriptionPlan])
async def get_available_plans(current_user = Depends(require_customer)):
    plans_cursor = db["plans"].find()
    plans = await plans_cursor.to_list(length=100)
    for plan in plans:
        plan.pop("_id", None)
    return plans

@router.post("/subscribe")
async def subscribe_to_plan(plan: models.PlanAssign, current_user = Depends(require_customer)):
    plan_doc = await db["plans"].find_one({"name": plan.plan})
    if not plan_doc:
        raise HTTPException(status_code=404, detail="Plan not found")
    zero_usage = {f"service{i}": 0 for i in range(1, 7)}
    await db["users"].update_one({"_id": current_user["_id"]}, {
        "$set": {
            "plan": plan.plan,
            "usage": zero_usage
        }
    })
    return {"detail": f"Subscribed to plan '{plan.plan}'"}

@router.get("/subscription")
async def get_subscription(current_user = Depends(require_customer)):
    plan_name = current_user.get("plan")
    if not plan_name:
        raise HTTPException(status_code=404, detail="No active subscription")
    plan_doc = await db["plans"].find_one({"name": plan_name})
    if not plan_doc:
        raise HTTPException(status_code=404, detail="Plan not found")
    usage = current_user.get("usage", {})
    quotas = {f"service{i}": plan_doc.get(f"service{i}_quota", 0) for i in range(1, 7)}
    remaining = {k: quotas[k] - usage.get(k, 0) for k in quotas}
    return {
        "plan": plan_name,
        "quotas": quotas,
        "usage": usage,
        "remaining_quota": remaining
    }
