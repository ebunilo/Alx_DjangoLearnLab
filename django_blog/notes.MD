# Notes on creating the Django Blog Project

## Create a virtual environment for python 3.10
PythonAnywhere hosting supports python 3.10 and below. Hence this project will be run on python 3.10

- bash python3.10 -m venv .venv
- source .venv/bin/activate

## Install Django
- pip install django

## Create project
- django-admin startproject django_blog

# Create apps
- python manage.py startapp blog
- python manage.py startapp users
- add the apps in the "Installed Apps" section of settings.py

# Create a Custom User called User
In users.models.py, create a User class that inherits from AbstractUser
- define email and username fields
- create a UserManager() class that inherits from BaseUserManager
- Define the creat_user() and create_superuser() methods inside the UserManager class.
- In settings.py point the default user to this User class as show below:
AUTH_USER_MODEL = users.User

## Create Post Model
In the blog.models.py, create the Post model

## Use postgresql database
Update settings.py to use PosgreSQL database.
- Create the database you want to use prior to running migrations. Else, it will throw error about not finding the database.
- sudo -u postgres psql
- CREATE DATABASE blog;


## addons
- pip install django-taggit (for Post tagging)
- pip install Pillow (for picture management)

