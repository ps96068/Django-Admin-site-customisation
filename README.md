# Django Admin site customisation

The project consists of the following:

1. **"accounts" application** - Custom user model inherited from `AbstractUser`.

2. **"admins" application** - This application customizes the **Django Admin Site** and automatically registers any new URL of the admin site without editing the `admins.urls.py` file, all exclusively using Django, without using additional tools.

   This application brings some essential modifications, according to the author's opinion, demonstrating the implementation of different admin sites (with different URLs) for various users with content administration roles. In the repository example, there are two URLs leading to the Django Admin Site:
   
   - **2.1 "localhost/super/admin"**
   - **2.2 "localhost/super/shop-admin"**

   Access to 2.1 is reserved only for superuser-type users, while access to 2.2 is allowed for superuser-type users and staff-type users. Staff users accessing the second URL gain access only to those models for which they have been granted permission by the superuser. All the magic happens in the "admin" package from "admins" application.

3. Two separate applications: **<apps/blog>** and **<apps/shop>** - Each of these applications defines several models. In the `admin.py` of each application, the models are added to Admin Site 2.2 (see point 2). Also, all models of the applications are automatically added to Admin Site 2.1 (see point 2).

## Requirements

- Python (version 3.11.7)
- Django (version 4.2.9)


## Installation

1. Clone this repository: `git clone https://github.com/username/project-name.git`
2. Navigate to the project directory: `cd project-name`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
    - For Windows: `venv\Scripts\activate`
    - For Linux/Mac: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Apply migrations: `python manage.py migrate`

## Usage

1. Run the Django development server: `python manage.py runserver`
2. Access the application in the browser at: `http://localhost:8000/`
3. Access the admin site in the browser at: `http://localhost:8000/super/admin`
4. Access the admin site in the browser at: `http://localhost:8000/super/shop-admin`


---
© 2024 - @ps96068