🛡️ Secure Multi-Tenant SaaS Backend
   
## 📌 Overview

A secure multi-tenant SaaS backend built using **Django** and **Django REST Framework**.
This project demonstrates schema-based tenant isolation, JWT authentication, role-based access control (RBAC), and secure REST APIs.
Each tenant operates within an isolated database schema ensuring zero data leakage.

---

## 🚀 Features

* Schema-based multi-tenancy using **django-tenants**
* JWT authentication with **SimpleJWT**
* Role-Based Access Control (ADMIN / USER)
* Tenant-aware Dashboard API
* User Management APIs (CRUD)
* Admin-only Audit Log system
* Secure RESTful APIs using DRF ViewSets & Serializers
* Permission-protected endpoints

---

## 🛠 Tech Stack

* Python
* Django
* Django REST Framework
* PostgreSQL
* django-tenants
* SimpleJWT

---

## 📂 Project Structure

```
accounts/   → Authentication, Users, RBAC permissions
core/       → Common APIs (Dashboard)
audit/      → Activity logging system
config/     → Project settings & routing
```

---

## ⚙️ Setup Instructions

1. Clone repository

```
git clone <your-repo-url>
cd saas-backend
```

2. Create virtual environment

```
python -m venv venv
source venv/bin/activate
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Run migrations

```
python manage.py migrate_schemas
```

5. Start development server

```
python manage.py runserver
```

---

## 🔐 Authentication

Obtain JWT token:

```
POST /api/token/
```

Body:

```
{
  "username": "admin",
  "password": "admin123"
}
```

Use token in headers:

```
Authorization: Bearer <ACCESS_TOKEN>
```

---

## 🌐 API Examples

### Dashboard API

```
GET /api/dashboard/
```

Response:

```
{
  "tenant": "Tenant One",
  "user": "admin",
  "role": "ADMIN"
}
```

### Users API (Admin Only)

```
GET /api/users/
POST /api/users/
PATCH /api/users/{id}/
DELETE /api/users/{id}/
```

### Audit Logs (Admin Only)

```
GET /api/audit-logs/
```

---

## 🧠 Key Concepts Implemented

* Multi-tenant architecture with schema isolation
* JWT-based authentication
* Role-based authorization
* REST API design using DRF ViewSets
* Serializer-based response structure


