# services.py – route handlers for Service APIs
from fastapi import APIRouter, Depends, HTTPException, status
from ..auth import get_current_user
from ..db import db

router = APIRouter()  # Create router instance

@router.get("/service1")
async def use_service1(current_user = Depends(get_current_user)):
    service = "service1"
    if current_user["role"] == "admin":
        return {"message": f"{service} accessed with admin privileges (unlimited)"}
    plan_name = current_user.get("plan")
    if not plan_name:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No active subscription plan")
    plan_doc = await db["plans"].find_one({"name": plan_name})
    if not plan_doc:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Subscription plan not found")
    allowed = plan_doc.get("service1_quota", 0)
    used = current_user.get("usage", {}).get("service1", 0)
    if used >= allowed:
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail=f"Quota exceeded for {service}")
    # Atomically increment usage if below quota
    result = await db["users"].update_one({"_id": current_user["_id"], "usage.service1": {"$lt": allowed}}, {"$inc": {"usage.service1": 1}})
    if result.modified_count == 0:
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail=f"Quota exceeded for {service}")
    new_used = used + 1
    remaining = allowed - new_used
    return {"message": f"{service} used successfully", "usage": new_used, "remaining_quota": remaining}

@router.get("/service2")
async def use_service2(current_user = Depends(get_current_user)):
    service = "service2"
    if current_user["role"] == "admin":
        return {"message": f"{service} accessed with admin privileges (unlimited)"}
    plan_name = current_user.get("plan")
    if not plan_name:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No active subscription plan")
    plan_doc = await db["plans"].find_one({"name": plan_name})
    if not plan_doc:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Subscription plan not found")
    allowed = plan_doc.get("service2_quota", 0)
    used = current_user.get("usage", {}).get("service2", 0)
    if used >= allowed:
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail=f"Quota exceeded for {service}")
    result = await db["users"].update_one({"_id": current_user["_id"], "usage.service2": {"$lt": allowed}}, {"$inc": {"usage.service2": 1}})
    if result.modified_count == 0:
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail=f"Quota exceeded for {service}")
    new_used = used + 1
    remaining = allowed - new_used
    return {"message": f"{service} used successfully", "usage": new_used, "remaining_quota": remaining}

@router.get("/service3")
async def use_service3(current_user = Depends(get_current_user)):
    service = "service3"
    if current_user["role"] == "admin":
        return {"message": f"{service} accessed with admin privileges (unlimited)"}
    plan_name = current_user.get("plan")
    if not plan_name:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No active subscription plan")
    plan_doc = await db["plans"].find_one({"name": plan_name})
    if not plan_doc:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Subscription plan not found")
    allowed = plan_doc.get("service3_quota", 0)
    used = current_user.get("usage", {}).get("service3", 0)
    if used >= allowed:
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail=f"Quota exceeded for {service}")
    result = await db["users"].update_one({"_id": current_user["_id"], "usage.service3": {"$lt": allowed}}, {"$inc": {"usage.service3": 1}})
    if result.modified_count == 0:
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail=f"Quota exceeded for {service}")
    new_used = used + 1
    remaining = allowed - new_used
    return {"message": f"{service} used successfully", "usage": new_used, "remaining_quota": remaining}

@router.get("/service4")
async def use_service4(current_user = Depends(get_current_user)):
    service = "service4"
    if current_user["role"] == "admin":
        return {"message": f"{service} accessed with admin privileges (unlimited)"}
    plan_name = current_user.get("plan")
    if not plan_name:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No active subscription plan")
    plan_doc = await db["plans"].find_one({"name": plan_name})
    if not plan_doc:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Subscription plan not found")
    allowed = plan_doc.get("service4_quota", 0)
    used = current_user.get("usage", {}).get("service4", 0)
    if used >= allowed:
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail=f"Quota exceeded for {service}")
    result = await db["users"].update_one({"_id": current_user["_id"], "usage.service4": {"$lt": allowed}}, {"$inc": {"usage.service4": 1}})
    if result.modified_count == 0:
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail=f"Quota exceeded for {service}")
    new_used = used + 1
    remaining = allowed - new_used
    return {"message": f"{service} used successfully", "usage": new_used, "remaining_quota": remaining}

@router.get("/service5")
async def use_service5(current_user = Depends(get_current_user)):
    service = "service5"
    if current_user["role"] == "admin":
        return {"message": f"{service} accessed with admin privileges (unlimited)"}
    plan_name = current_user.get("plan")
    if not plan_name:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No active subscription plan")
    plan_doc = await db["plans"].find_one({"name": plan_name})
    if not plan_doc:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Subscription plan not found")
    allowed = plan_doc.get("service5_quota", 0)
    used = current_user.get("usage", {}).get("service5", 0)
    if used >= allowed:
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail=f"Quota exceeded for {service}")
    result = await db["users"].update_one({"_id": current_user["_id"], "usage.service5": {"$lt": allowed}}, {"$inc": {"usage.service5": 1}})
    if result.modified_count == 0:
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail=f"Quota exceeded for {service}")
    new_used = used + 1
    remaining = allowed - new_used
    return {"message": f"{service} used successfully", "usage": new_used, "remaining_quota": remaining}

@router.get("/service6")
async def use_service6(current_user = Depends(get_current_user)):
    service = "service6"
    if current_user["role"] == "admin":
        return {"message": f"{service} accessed with admin privileges (unlimited)"}
    plan_name = current_user.get("plan")
    if not plan_name:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No active subscription plan")
    plan_doc = await db["plans"].find_one({"name": plan_name})
    if not plan_doc:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Subscription plan not found")
    allowed = plan_doc.get("service6_quota", 0)
    used = current_user.get("usage", {}).get("service6", 0)
    if used >= allowed:
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail=f"Quota exceeded for {service}")
    result = await db["users"].update_one({"_id": current_user["_id"], "usage.service6": {"$lt": allowed}}, {"$inc": {"usage.service6": 1}})
    if result.modified_count == 0:
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail=f"Quota exceeded for {service}")
    new_used = used + 1
    remaining = allowed - new_used
    return {"message": f"{service} used successfully", "usage": new_used, "remaining_quota": remaining}
