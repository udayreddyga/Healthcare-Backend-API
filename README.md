# Healthcare Backend API

A Django REST Framework backend for healthcare management system with doctors, patients, and appointment mappings.

## 🚀 Features

- **Doctor Management** - CRUD operations for doctors
- **Patient Management** - CRUD operations for patients  
- **Appointment System** - Map patients to doctors with appointment dates
- **RESTful APIs** - Fully functional REST APIs
- **Admin Panel** - Django admin for data management
- **Authentication** - Token-based authentication
- **PostgreSQL** - Production-ready database

## 🛠️ Tech Stack

- **Backend:** Django 4.2+, Django REST Framework
- **Database:** PostgreSQL (Production), SQLite (Development)
- **Authentication:** Token Authentication
- **API Documentation:** Built-in DRF Browsable API

## 📋 Prerequisites

- Python 3.8+
- PostgreSQL (for production)
- Git

## ⚡ Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/healthcare-backend.git
cd healthcare-backend
2. Create Virtual Environment
bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
3. Install Dependencies
bash
pip install -r requirements.txt
4. Database Setup
For Development (SQLite):

bash
python manage.py migrate
For Production (PostgreSQL):
Update DATABASES in healthcare/settings.py with your PostgreSQL credentials, then:

bash
python manage.py migrate
5. Create Superuser
bash
python manage.py createsuperuser
6. Run Development Server
bash
python manage.py runserver
Visit: http://localhost:8000
