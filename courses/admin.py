from django.contrib import admin
from .models import Course, Course_category, Course_subcategory, Course_resource

# Register your models here.
admin.site.register(Course)
admin.site.register(Course_category)
admin.site.register(Course_subcategory)
admin.site.register(Course_resource)