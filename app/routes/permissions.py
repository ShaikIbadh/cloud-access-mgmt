from fastapi import APIRouter, HTTPException, Depends, status
from app.auth import get_current_admin
from app.db import db
from pydantic import BaseModel
from bson import ObjectId

router = APIRouter()

class PermissionModel(BaseModel):
    name: str
    endpoint: str
    description: str

@router.post("/admin/permissions")
async def add_permission(permission: PermissionModel, admin=Depends(get_current_admin)):
    existing = await db["permissions"].find_one({"name": permission.name})
    if existing:
        raise HTTPException(400, detail="Permission already exists")
    result = await db["permissions"].insert_one(permission.dict())
    return {"message": "Permission added", "id": str(result.inserted_id)}

@router.put("/admin/permissions/{permission_id}")
async def update_permission(permission_id: str, update: PermissionModel, admin=Depends(get_current_admin)):
    result = await db["permissions"].update_one({"_id": ObjectId(permission_id)}, {"$set": update.dict()})
    if result.modified_count == 0:
        raise HTTPException(404, detail="Permission not found or no change")
    return {"message": "Permission updated"}

@router.delete("/admin/permissions/{permission_id}")
async def delete_permission(permission_id: str, admin=Depends(get_current_admin)):
    result = await db["permissions"].delete_one({"_id": ObjectId(permission_id)})
    if result.deleted_count == 0:
        raise HTTPException(404, detail="Permission not found")
    return {"message": "Permission deleted"}
