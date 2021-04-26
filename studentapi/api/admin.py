from django.contrib import admin
from .models import Student, Guardian

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ['first_name', 'last_name', 'standard', 'evaluation', 'city', 'country', 'active', 'joined_on']

class GuardianAdmin(admin.ModelAdmin):
    model = Guardian
    list_display = ['first_name', 'last_name', 'student', 'relation', 'address', 'mobile_number']


admin.site.register(Student, StudentAdmin)
admin.site.register(Guardian, GuardianAdmin)
