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
└── README.txt

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

Open Swagger UI in Your Browser
     http://127.0.0.1:8000/docs

Authorize Using API Key
     pw: admin123
Then test all Admin and Customer endpoints from the Swagger interface.
