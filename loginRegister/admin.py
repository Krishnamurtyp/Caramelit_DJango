from django.contrib import admin
from .models import User, entity, instructor, adminUser

# Register your models here.
admin.site.register(User)
admin.site.register(entity)
admin.site.register(instructor)
admin.site.register(adminUser)