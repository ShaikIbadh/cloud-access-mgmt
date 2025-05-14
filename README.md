# ☁️ Cloud Service Access Management System

### Team Member:
- **Safdar Ibadh Shaik**  
  **CWID**: 875437477  
  _(Individual Project)_

---

## 📁 Folder Structure

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

## 🚀 How to Run

### 1️⃣ Create and Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Start MongoDB Locally (Homebrew - macOS)
```bash
brew tap mongodb/brew
brew install mongodb-community
brew services start mongodb/brew/mongodb-community
```

### 4️⃣ Confirm MongoDB Is Running
```bash
mongosh
```

### 5️⃣ Insert Admin User in MongoDB
```javascript
use cloud_service_db
db.users.insertOne({
  name: "AdminSafdar",
  role: "admin",
  api_key: "admin123"
})
```

### 6️⃣ Run the FastAPI App
```bash
uvicorn app.main:app --reload
```

### 7️⃣ Open Swagger UI in Your Browser
```
http://127.0.0.1:8000/docs
```

### 8️⃣ Authorize Using API Key
- Use the 🔒 **Authorize** button
- Enter:
  ```
  admin123
  ```

You can now test all **Admin** and **Customer** endpoints from the Swagger interface.

---

## ✅ Project Summary

This project implements role-based access to cloud services using FastAPI and MongoDB. Admins can manage plans and users, while customers subscribe to plans and access quota-limited services.

---

