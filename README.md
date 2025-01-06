# FastAPI Company

## درباره پروژه | About the Project

این پروژه شامل یک API برای مدیریت موجودیت‌های شرکتی است که با استفاده از **FastAPI** ساخته شده و یک رابط کاربری نمایشی با استفاده از **Streamlit** ارائه می‌دهد.  
This project provides an API for managing company entities, built with **FastAPI** and accompanied by a demo frontend using **Streamlit**.

## ویژگی‌ها | Features

- **FastAPI**: فریمورک قدرتمند برای ساخت API.  
  A powerful framework for building APIs.
- **SQLAlchemy**: مدیریت تعاملات با پایگاه داده.  
  Manages database interactions.
- **Alembic**: مدیریت مهاجرت‌های پایگاه داده.  
  Handles database migrations.
- **Passlib**: هش کردن رمز عبور.  
  Manages password hashing.
- **Streamlit**: رابط کاربری ساده و تعاملی.  
  Provides a simple and interactive frontend interface.

## نصب و راه‌اندازی | Installation

1. **کلون کردن مخزن | Clone the repository**:

   ```bash
   git clone https://github.com/sorna-fast/fast_api_company.git
   cd fast_api_company
   ```
   
2.ایجاد و فعال‌سازی محیط مجازی | Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3.نصب وابستگی‌ها | Install the dependencies:
```
pip install -r requirements.txt
```

## نحوه استفاده | Usage
1.اجرای مهاجرت‌های پایگاه داده | Apply database migrations:
```
alembic upgrade head
```
2.اجرای برنامه | Run the application:
```
python run.py
```
3.دسترسی به رابط کاربری | Access the frontend:

مرورگر خود را باز کرده و به آدرس http://localhost:8501 بروید.
Open your browser and navigate to http://localhost:8501.


## config

### 1.از کردن فایل main.py:

فایل main.py را در ویرایشگر کد خود باز کنید.
### 2.یافتن بخش تنظیمات پایگاه داده:

در این فایل، به دنبال بخشی بگردید که اتصال به پایگاه داده تنظیم شده است. معمولاً چیزی شبیه به این خواهد بود:

```
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
```
### 3.ویرایش تنظیمات پایگاه داده:

مقدار SQLALCHEMY_DATABASE_URL را با اطلاعات پایگاه داده خود جایگزین کنید. به عنوان مثال، برای استفاده از یک پایگاه داده PostgreSQL:
```
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/dbname"
```
جزئیات مربوط به user، password، localhost و dbname را با مقادیر مناسب جایگزین کنید.

### 4.ذخیره تغییرات و اجرای مهاجرت‌ها:

پس از اعمال تغییرات، فایل را ذخیره کنید.

سپس، برای اعمال مهاجرت‌های پایگاه داده، دستور زیر را اجرا کنید:
```
alembic upgrade head
```
این دستور ساختار پایگاه داده را به‌روز می‌کند.

### 5.اجرای برنامه:

اکنون می‌توانید برنامه را با دستور زیر اجرا کنید:
```
python run.py
```

