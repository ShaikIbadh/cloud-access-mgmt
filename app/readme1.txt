Team members
  Safdar Ibadh Shaik(Individual project)
  CWID : 875437477
  
Folder Structure

cloud-access-mgmt/
├── app/
│   ├── main.py
│   ├── db.py
│   ├── auth.py
│   ├── models.py
│   └── routes/
│       ├── admin.py
│       ├── customer.py
│       └── services.py
├── requirements.txt
└── readme1.txt

HOW TO RUN 

Create and Activate a Virtual Environment
   python3 -m venv venv
   source venv/bin/activate

Install Dependencies
   pip install -r requirements.txt

Start MongoDB Locally
    brew tap mongodb/brew
    brew install mongodb-community
    brew services start mongodb/brew/mongodb-community
To confirm MongoDB is running:
    mongosh
Insert Admin User in MongoDB
   use cloud_service_db
   db.users.insertOne({
     name: "AdminSafdar",
      role: "admin",
      api_key: "admin123"
    })

Run the FastAPI App
    uvicorn app.main:app --reload

How to Use the API

Once the app is running and you’ve opened Swagger UI at:

http://127.0.0.1:8000/docs
Follow these steps:

Click the Authorize button on the top right.
Enter your API key admin123 for Admin users or customer keys created via /admin/users.
Test available API endpoints:
Admin API Examples:

POST /admin/plans → Create a new subscription plan
POST /admin/users → Create a new customer user
PUT /admin/users/{id} → Update customer plan
Customer API Examples:

GET /customer/plans → View all available plans
POST /customer/subscribe → Subscribe to a selected plan
GET /customer/subscription → View usage & remaining quota
Cloud Services (Quota-Protected):

GET /services/service1 → Simulate using Service 1
...
GET /services/service6 → Simulate using Service 6
If a user exceeds their plan quota, the API will respond with:

429 Too Many Requests
Then test all Admin and Customer endpoints from the Swagger interface.
