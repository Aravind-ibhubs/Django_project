# Django_project

## Run a project : `py manage.py runserver`

## Create a new project : `django-admin startproject project-name`

------------------------------------

## Create a new app

An app is a web application that has a specific meaning in your project, like a home page, a contact form, or a members database.

### code : `py manage.py startapp app-name`

------------------------------------

## Migrating the changes : `py manage.py migrate`
------------------------------------------------------------
## Made migrations in syallabus : `py .\manage.py makemigrations syallabus`
---------------------------------------------------------------
##  view SQL : `py manage.py sqlmigrate syallabus 0001`

# Data bases
- Opening a shell : `py manage.py shell`
-imports : `from syallabus.models import Books`
-Get data : `Books.objects.all()`
-Get data for more value : `Books.objects.all().values()`
-** Inserting new data **
    1. Assigning data = `data = Books(bookname="name",author="name")`
    2. Save the data = `data.save()`
-** Updating existing data
    1. Get the specific data = `con = Books.objects.all().values()[4]`
    2. Check the data  = `con['bookname']`
    3. Changing the name = `con['bookname'] = "Howla" `
-** Deleting data **
    1. Get the specific data = `data_del = Books.objects.get(id=3)`
    2.deleting =   `data_del.delete()`
-** Updating the newly added colums values
    1. get the value = `x = Books.objects.all()[3]`
    2. updating value = `x['cost'] = 234`
    3. Saving the cost  = `x.save()`

