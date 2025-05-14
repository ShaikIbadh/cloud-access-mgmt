#  Cloud Service Access Management System

### Team Member:
- **Safdar Ibadh Shaik**  
  **CWID**: 875437477  
  _(Individual Project)_

---
## Project Description

This project simulates a cloud service platform backend, developed using **FastAPI** and **MongoDB**.
It allows:
- Admins to create and manage subscription plans, register users, and assign quotas.
- Customers to subscribe to available plans and consume cloud services within their allocated quotas.
- Enforced role-based access control (RBAC) and real-time usage tracking.

##  Folder Structure

```
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
```

---

##  How to Run

### 1 Create and Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2 Install Dependencies
```bash
pip install -r requirements.txt
```

### 3 Start MongoDB Locally (Homebrew - macOS)
```bash
brew tap mongodb/brew
brew install mongodb-community
brew services start mongodb/brew/mongodb-community
```

### 4 Confirm MongoDB Is Running
```bash
mongosh
```

### 5 Insert Admin User in MongoDB
```javascript
use cloud_service_db
db.users.insertOne({
  name: "AdminSafdar",
  role: "admin",
  api_key: "admin123"
})
```

### 6 Run the FastAPI App
```bash
uvicorn app.main:app --reload
```

### 7 Open Swagger UI in Your Browser
```
http://127.0.0.1:8000/docs
```

### 8 Authorize Using API Key
- Use the  **Authorize** button
- Enter:
  ```
  admin123
  ```


You can now test all **Admin** and **Customer** endpoints from the Swagger interface.

---

