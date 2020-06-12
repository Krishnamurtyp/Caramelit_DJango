from django.db import models
from django.utils import timezone

# Course Category
class Course_category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    date_of_creation = models.DateTimeField(default=timezone.now)
 
# Course Subcategory
class Course_subcategory(models.Model):
    subcategory_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Course_category, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=100)
    date_of_creation = models.DateTimeField(default=timezone.now)

# Course
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    subcategory = models.ForeignKey(Course_subcategory, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=100)
    category_name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    date_of_creation = models.DateTimeField(default=timezone.now)
    course_description = models.TextField(default="")
    course_difficulty = models.CharField(max_length=30)

# Course resources
class Course_resource(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    resourse_name = models.CharField(max_length=100)
    resourse_link = models.CharField(max_length=100)
    resourse_length = models.CharField(max_length=10)
    date_of_creation = models.DateTimeField(default=timezone.now)