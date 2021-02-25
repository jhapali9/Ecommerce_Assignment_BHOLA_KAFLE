# DJANGO LAB EXAM

# Installing Django

## Setup (using virtual environemnt)

- Installing virtual environment
	> apt install python3-venv

- switching to virtual environment
	> python3.8 -m venv my_env
- activating virtual environment
	> source my_env/bin/activate
	
- installing django
> pip install django

## Creating lab_exam project
- Creating virtual environment
	> python3.8 -m venv my_env
	
- Activating virtual environment
	> source my_env/bin/activate 
- Installing django
	> pip install django
- Creating our project 
	> django-admin startproject LabExam
-  Running Migrations
	> python manage.py migrate 
- Creating superuser
	> python manage.py createsuperuser
	-  A username, an email address, and a password for your user.
	-   An email
	-   A password (containing at least 8 characters)
- Creating lab_exam app
	> python manage.py startapp lab_exam

## Creating lab_exam model
- Inside lab_exam/models.py
	
	from django.db import models

## Creating LabExam Model
### Inside lab_exam/models.py

class  LabExam(models.Model):

	exam_date = models.DateField()

	exam_name = models.CharField(max_length=255)

	exam_description = models.TextField()

	total_marks = models.FloatField(null=True, blank=True)

	pass_marks = models.FloatField(null=True, blank=True)

	exam_status = models.BooleanField()

  
	def  __str__(self):

		return  self.exam_name

## Migration
- Creating migration
	> python manage.py makemigrations lab_exam

## Migrating to sqlite database
- By default django comes with sqlite database which is located inside root project folder as db.sqlite3 file
- Migrating to sqlite
	> python manage.py migrate


## Registering app
- Inside bhola_exam/settings.py
	> INSTALLED_APPS = [

				........

				'lab_exam'

				]
				
## Registering site in admin
- Inside lab_exam/admin.py
```
from django.contrib import admin

from .models import LabExam

admin.site.register(LabExam)
	  
```
## Running the server and doing CRUD operations
- Run the server
	> python manage.py runserver
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 25, 2021 - 02:36:57
Django version 3.1.7, using settings 'bhola_lab.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
- Go to http://127.0.0.1:8000/admin
- Login with admin credentials and manage some crud operations on lab_exam


  
# Pushing the project to github
## Creating a repository
- Login to github and create repository named as Ecommerce_Assignment_BHOLA_KAFLE
## Adding remote repo 
```
git remote add origin https://github.com/jhapali9/Ecommerce_Assignment_BHOLA_KAFLE.git
```
## Adding files to staging area
```
	git add .
```
## Commiting the changed file
```
	git commit -m "First Commit for Lab Exam"
```
## Pushing the file to github
```
	git push 
```
## Creating a readme.md file and push changes
- Create a file readme.md inside project root folder
- add this file in stating area
- commit the change
- push to github





