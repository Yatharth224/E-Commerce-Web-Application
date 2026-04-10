# 🛒 E-Commerce Backend System (Django + DRF)

## 📌 Overview

This project is a production-ready **E-Commerce Backend System** built using **Django** and **Django REST Framework (DRF)**. It demonstrates a scalable, secure, and high-performance backend architecture with real-world features such as authentication, caching, background processing, and deployment strategies.

---

## 🚀 Key Features

* Django fundamentals with modular architecture
* RESTful API development using DRF
* JWT-based authentication & authorization
* Background task processing with Celery
* Redis-based caching
* Automated testing (unit + performance)
* Logging & monitoring
* Production-ready deployment

---

## 🏗️ System Architecture

### High-Level Architecture

```
Client (React / Web / Mobile)
        |
        v
API Layer (Django REST Framework)
        |
        v
Business Logic Layer (Services / Managers)
        |
        v
Database Layer (PostgreSQL / MySQL)

Additional Components:
- Redis (Caching + Celery Broker)
- Celery Workers (Async Tasks)
- Nginx + Gunicorn (Production Server)
```

---

## 📂 Project Structure

```
ecommerce_project/
│
├── manage.py
├── ecommerce_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── apps/
│   ├── users/
│   ├── products/
│   ├── orders/
│   ├── cart/
│   └── payments/
│
├── core/
│   ├── utils/
│   ├── permissions/
│   └── services/
│
├── celery.py
├── requirements.txt
└── Dockerfile
```

---

## 🧠 Core Concepts Implemented

### 1. Django Fundamentals

* Models for database schema
* Views & URL routing
* Django Admin customization
* ORM queries & optimization

Example:

```python
class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
```

---

### 2. Django REST Framework (DRF)

* Serializers for data transformation
* ViewSets & APIViews
* Pagination, filtering, searching

Example:

```python
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

---

### 3. Authentication & Security

* JWT Authentication
* Access & Refresh Tokens
* Role-based permissions

Flow:

```
User Login → Generate Access Token → Access Protected APIs
            → Refresh Token → Get New Access Token
```

---

### 4. Background Tasks (Celery)

Used for:

* Sending emails
* Order processing
* Notifications

Example:

```python
@shared_task
def send_order_email(order_id):
    # async email logic
    pass
```

---

### 5. Caching (Redis)

* Improves performance
* Reduces DB load

Example:

```python
@cache_page(60 * 5)
def product_list(request):
    return Response(data)
```

---

### 6. Testing Strategy

* Unit Testing (Django TestCase)
* API Testing (DRF APITestCase)
* Performance Testing

---

### 7. Logging & Monitoring

* Structured logging
* Error tracking
* Debug vs Production logs

---

## ⚙️ Database Design

### Entities:

* User
* Product
* Category
* Cart
* Order
* Payment

### Relationships:

* User → Orders (1:N)
* Order → Products (M:N)
* Product → Category (N:1)

---

## 🔄 API Design

### Sample Endpoints:

| Method | Endpoint         | Description   |
| ------ | ---------------- | ------------- |
| GET    | /api/products/   | List products |
| POST   | /api/auth/login/ | User login    |
| POST   | /api/orders/     | Create order  |
| GET    | /api/cart/       | View cart     |

---

## 🔁 Application Flow (End-to-End)

### 1. User Authentication Flow

```
User → Login Request (username, password)
     → Django Auth + JWT
     → Access Token + Refresh Token Generated
     → Client Stores Token
     → User Accesses Protected APIs using Access Token
     → Token Expired → Use Refresh Token → New Access Token
```

---

### 2. Product Browsing Flow

```
User → Request Product List
     → DRF ViewSet
     → Check Cache (Redis)
         → If Cached → Return Response
         → Else → Fetch from DB → Store in Cache → Return
```

---

### 3. Add to Cart Flow

```
User → Add Product to Cart
     → API Validates Product & Stock
     → Cart Model Updated
     → Response Sent to Client
```


---

### 4. Order Placement Flow (Critical Flow)

```
User → Place Order
     → Validate Cart Items
     → Create Order in DB
     → Deduct Stock
     → Trigger Celery Task
         → Send Email / Notification
     → Return Order Confirmation
```

### 5. Background Task Flow (Celery)

```
Django App → Sends Task to Redis Broker
           → Celery Worker Picks Task
           → Executes (Email / Notification / Processing)
           → Updates Status (if required)
```

---
