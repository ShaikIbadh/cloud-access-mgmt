# db.py – MongoDB connection using Motor
from motor.motor_asyncio import AsyncIOMotorClient  # Async MongoDB client from Motor

MONGO_URI = "mongodb://localhost:27017"
client = AsyncIOMotorClient  # Async MongoDB client from Motor(MONGO_URI)
db = client["cloud_service_db"]  # Database for the cloud access system
