from django.db import models
from django.utils import timezone

# Student user
class User(models.Model):
    student_id = models.AutoField(primary_key=True)
    user_type = models.CharField(max_length=12, default='')
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=100, unique=True, default='')
    phone = models.BigIntegerField()
    birth_date = models.DateField()
    country = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=100, default='')
    highest_qualification = models.CharField(max_length=100, default='')
    university_name = models.CharField(max_length=100, default='')
    specialisation = models.CharField(max_length=100, default='')
    skill_set = models.CharField(max_length=100)
    profileImg = models.CharField(max_length=100, default='photo.jpg')
    date_of_reg = models.DateTimeField(default=timezone.now)
    no_of_courses = models.IntegerField(default=0)
    password = models.CharField(max_length=100)
    organisation= models.CharField(max_length=100, default='')
    experience= models.CharField(max_length=100, default='')
    specialisation= models.CharField(max_length=100, default='')
    pastOrganisation=models.CharField(max_length=100, default='')
    college_state = models.CharField(max_length=100, default='')
    college = models.CharField(max_length=100)

class instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.BigIntegerField()
    subjects = models.CharField(max_length=100)
    state = models.CharField(max_length=100, default='')
    job_organisation_name = models.CharField(max_length=200, default='')
    job_experience = models.CharField(max_length=100, default='')
    job_location = models.CharField(max_length=100, default='')
    job_state = models.CharField(max_length=100, default='')
    job_type = models.CharField(max_length=8)
    skills = models.CharField(max_length=100, default='')
    experience = models.CharField(max_length=100)
    description = models.TextField()
    profileImg = models.CharField(max_length=100, default='photo.jpg')
    date_of_reg = models.DateTimeField(default=timezone.now)
    password = models.CharField(max_length=100)

class entity(models.Model):
    entity_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=12)
    birth_date = models.DateField()
    college_name = models.CharField(max_length=100, default='')
    university_name = models.CharField(max_length=100, default='')
    university_skill = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=100, unique=True)
    phone = models.BigIntegerField()
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    skill_set = models.CharField(max_length=100)
    description = models.TextField()
    organisation_name = models.CharField(max_length=100, default='')
    organisation_email = models.EmailField(max_length=100, unique=True, default='')
    profileImg = models.CharField(max_length=100, default='photo.jpg')
    date_of_reg = models.DateTimeField(default=timezone.now)
    password = models.CharField(max_length=100)

class adminUser(models.Model):
    admin_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    address = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    profileImg = models.CharField(max_length=100, default='photo.jpg')
    date_of_reg = models.DateTimeField(default=timezone.now)
    password = models.CharField(max_length=100)
  
class program_details(models.Model):
    
    program=models.CharField(max_length=200)

class subprogram_details(models.Model):
    
    subprogram_name=models.CharField(max_length=200)
    
    program=models.CharField(max_length=200)

class course_names(models.Model):
    
    course_name=models.CharField(max_length=200)
    
    subprogram=models.CharField(max_length=200)
    img = models.ImageField(upload_to="pics")