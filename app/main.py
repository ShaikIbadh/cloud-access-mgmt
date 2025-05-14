# main.py – FastAPI app setup and router registration
from fastapi import FastAPI
from app.routes.customer import router as customer_router
from app.routes.admin import router as admin_router
from app.routes.services import router as services_router
from app.db import client

app = FastAPI()  # Initialize FastAPI app

# Register route with FastAPI
app.include_router(admin_router, prefix="/admin", tags=["Admin"])
# Register route with FastAPI
app.include_router(customer_router, prefix="/customer", tags=["Customer"])
# Register route with FastAPI
app.include_router(services_router, prefix="/services", tags=["Services"])

# Gracefully close DB connection on shutdown
@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
