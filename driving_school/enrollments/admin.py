# Description: This file contains the admin configuration for the enrollments app.
from django.contrib import admin
from .models import Student, ClassSchedule, Enrollment # imports the Student, ClassSchedule, and Enrollment models

admin.site.register(Student) # registers the Student model with the admin site
admin.site.register(ClassSchedule) # registers the ClassSchedule model with the admin site  
admin.site.register(Enrollment) # registers the Enrollment model with the admin site    
# The code above registers the Student, ClassSchedule, and Enrollment models with the admin site, allowing them to be managed through the Django admin interface.
