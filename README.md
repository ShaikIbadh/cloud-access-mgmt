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

## 🔧 How to Use the API

Once the app is running and you’ve opened Swagger UI at:
```
http://127.0.0.1:8000/docs
```

Follow these steps:

1. Click the 🔒 **Authorize** button on the top right.
2. Enter your API key `admin123` for Admin users or customer keys created via `/admin/users`.
3. Test available API endpoints:

###  Admin API Examples:
- `POST /admin/plans` → Create a new subscription plan
- `POST /admin/users` → Create a new customer user
- `PUT /admin/users/{id}` → Update customer plan

###  Customer API Examples:
- `GET /customer/plans` → View all available plans
- `POST /customer/subscribe` → Subscribe to a selected plan
- `GET /customer/subscription` → View usage & remaining quota

###  Cloud Services (Quota-Protected):
- `GET /services/service1` → Simulate using Service 1
- ...
- `GET /services/service6` → Simulate using Service 6

❗ If a user exceeds their plan quota, the API will respond with:
```
429 Too Many Requests
```
---

