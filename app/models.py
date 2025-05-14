from pydantic import BaseModel, Field
from typing import Optional

class SubscriptionPlan(BaseModel):
    name: str
    service1_quota: int = Field(..., ge=0)
    service2_quota: int = Field(..., ge=0)
    service3_quota: int = Field(..., ge=0)
    service4_quota: int = Field(..., ge=0)
    service5_quota: int = Field(..., ge=0)
    service6_quota: int = Field(..., ge=0)

class Usage(BaseModel):
    service1: int = 0
    service2: int = 0
    service3: int = 0
    service4: int = 0
    service5: int = 0
    service6: int = 0

class UserCreate(BaseModel):
    name: str
    plan: Optional[str] = None  # Plan name to assign (optional)

class PlanAssign(BaseModel):
    plan: str

class UserOut(BaseModel):
    id: str
    name: str
    role: str
    api_key: str
    plan: Optional[str] = None
    usage: Usage
