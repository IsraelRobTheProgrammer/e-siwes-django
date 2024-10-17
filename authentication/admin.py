from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
from .models import Student

# admin.site.register(Student)


# Define an inline admin descriptor for Student model
# which acts a bit like a singleton
class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = "student"


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [StudentInline]


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
