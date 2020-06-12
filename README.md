# Caramelit_Backend
Code for the Caramel IT Academy's Website

## Location of Templates
All the static pages i.e. the main page for the Caramel IT website along with academy, consortium etc. pages can be found in the django App staticHome<br />

A different App for handing User login and registration is created with name loginRegister<br />
Schema for user profiles can be found in models.py file under the loginRegister directory<br />

Courses are handled by the app named courses under the directory of the same name i.e. courses.<br />
Database schema for courses, course category, sub category etc can be found in models.py file under courses directory.<br />

## Logic for each webpage
Views.py file under every app directory contains the logic for user authorization, registration, courses etc.<br />
urls.py file under the djangoApp directory contains all the defined urls that the app supports.<br /> 

## Changin Database from mysql to MongoDB
Changing the database in django is fairly simple and very convenient.<br />
Django has its own ORM(Object Relational Mapper), which does convertion of logic into SQL/NoSQL queries for us.<br />
In short, we don't need to know database query language at all. We can simply define models as class in models.py file in each app and use those classes and their predefined functions to work in database. The database queries will be handled by Django for us.<br />
To Change the type of database we simply need to go to setting.py file under djangoApp directory and change the value of 'DATABASES' variable.<br />
Using this we can simply change the database without changing any of the code in our django app.<br />

## Important Details
This app is still in development and need a few more modifications here and there to make it ready for deployment.<br />