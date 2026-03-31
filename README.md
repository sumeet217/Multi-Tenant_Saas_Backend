# 🛡️ Secure Multi-Tenant SaaS Backend

## 📌 Overview

A secure multi-tenant SaaS backend built using **Django 6.0** and **Django REST Framework**.
This project demonstrates schema-based tenant isolation, JWT authentication, role-based access control (RBAC), and secure REST APIs.
Each tenant operates within an isolated database schema ensuring zero data leakage.

---

## 🚀 Features

- Schema-based multi-tenancy using **django-tenants**
- JWT authentication with **SimpleJWT**
- Role-Based Access Control (ADMIN / MANAGER / USER / VIEWER)
- Tenant-aware Dashboard API
- User Management APIs (CRUD)
- Admin-only Audit Log system
- Secure RESTful APIs using DRF ViewSets & Serializers
- Permission-protected endpoints
- Dockerized development environment

---

## 🛠 Tech Stack

| Technology              | Purpose            |
| ----------------------- | ------------------ |
| Python 3.12             | Runtime            |
| Django 6.0              | Web framework      |
| Django REST Framework   | API layer          |
| PostgreSQL 15           | Database           |
| django-tenants          | Multi-tenancy      |
| SimpleJWT               | JWT authentication |
| Docker & Docker Compose | Containerization   |

---

## 📂 Project Structure

```
saas-backend/
├── accounts/       → Authentication, Users, RBAC permissions
├── core/           → Common APIs (Dashboard, Admin-only)
├── audit/          → Activity logging system
├── tenants/        → Tenant & Domain models
├── config/         → Project settings & routing
├── docker-compose.yml
├── dockerfile
├── requirements.txt
├── .env
└── manage.py
```

---

## ⚙️ Setup Instructions

### Prerequisites

- Python 3.12+
- PostgreSQL (local or via Docker)

### 1. Clone Repository

```bash
git clone <your-repo-url>
cd saas-backend
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

Copy the example env file and update values:

```bash
cp example.env .env
```

Edit `.env` with your database credentials:

```env
SECRET_KEY='your-secret-key'
DEBUG=True
DB_NAME=saasdb
DB_USER=saasuser
DB_PASSWORD=saaspass
DB_HOST=localhost
DB_PORT=5432
```

### 5. Start PostgreSQL (Docker)

```bash
docker-compose up -d db
```

### 6. Run Migrations

```bash
python manage.py migrate_schemas --shared
```

### 7. Create Public Tenant

A public tenant is required for `django-tenants` to resolve `localhost`:

```bash
python manage.py shell -c "
from tenants.models import Client, Domain
tenant = Client(schema_name='public', name='Public Tenant')
tenant.save()
Domain.objects.create(domain='localhost', tenant=tenant, is_primary=True)
print('Public tenant created!')
"
```

### 8. Create Superuser

```bash
python manage.py createsuperuser
```

### 9. Start Development Server

```bash
python manage.py runserver
```

---

## 🔐 Authentication

### Obtain JWT Token

```
POST /api/auth/token/
```

**Request Body:**

```json
{
  "username": "admin",
  "password": "your-password"
}
```

**Response:**

```json
{
  "access": "<ACCESS_TOKEN>",
  "refresh": "<REFRESH_TOKEN>"
}
```

### Refresh Token

```
POST /api/auth/token/refresh/
```

**Request Body:**

```json
{
  "refresh": "<REFRESH_TOKEN>"
}
```

### Use Token in Headers

```
Authorization: Bearer <ACCESS_TOKEN>
```

---

## 🌐 API Endpoints

### Auth & Core

| Method | Endpoint                   | Description         | Access        |
| ------ | -------------------------- | ------------------- | ------------- |
| POST   | `/api/auth/token/`         | Obtain JWT token    | Public        |
| POST   | `/api/auth/token/refresh/` | Refresh JWT token   | Public        |
| GET    | `/api/auth/dashboard/`     | Tenant dashboard    | Authenticated |
| GET    | `/api/auth/admin-only/`    | Admin-only endpoint | Admin         |

### User Management

| Method | Endpoint                    | Description      | Access |
| ------ | --------------------------- | ---------------- | ------ |
| GET    | `/api/accounts/users/`      | List all users   | Admin  |
| POST   | `/api/accounts/users/`      | Create user      | Admin  |
| GET    | `/api/accounts/users/{id}/` | Get user details | Admin  |
| PATCH  | `/api/accounts/users/{id}/` | Update user      | Admin  |
| DELETE | `/api/accounts/users/{id}/` | Delete user      | Admin  |

### Audit Logs

| Method | Endpoint                      | Description     | Access |
| ------ | ----------------------------- | --------------- | ------ |
| GET    | `/api/audit/audit-logs/`      | List audit logs | Admin  |
| GET    | `/api/audit/audit-logs/{id}/` | Get log details | Admin  |

---

## 🐳 Docker Setup

Run the entire stack with Docker Compose:

```bash
docker-compose up --build
```

This starts:

- **PostgreSQL 15** on port `5432`
- **Django dev server** on port `8000`

---

## 🔑 RBAC Roles

| Role      | Permissions                               |
| --------- | ----------------------------------------- |
| `ADMIN`   | Full access to all endpoints              |
| `MANAGER` | Access to admin + manager level endpoints |
| `USER`    | Standard user access                      |
| `VIEWER`  | Read-only access                          |

---

## 🧠 Key Concepts Implemented

- Multi-tenant architecture with PostgreSQL schema isolation
- JWT-based stateless authentication
- Hierarchical role-based authorization
- REST API design using DRF ViewSets & Serializers
- Serializer-based response structure
- Tenant-aware request middleware
- Audit logging for accountability
