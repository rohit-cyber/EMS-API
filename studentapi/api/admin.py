from django.conf.urls import url
from django.contrib import admin
from .models import Student, Guardian
from django.utils.html import format_html
from django.urls import reverse

# Register your models here.

class GuardianInlineAdmin(admin.TabularInline):
    model = Guardian

class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ['id','first_name','email', 'last_name', 'standard', 'evaluation', 'city', 'country', 'active', 'send_mail_button' , 'joined_on']
    inlines = [GuardianInlineAdmin]

    def send_mail_button(self,obj):
        button_url = reverse('particular_send_mail', args=[obj.pk])
        return format_html('<a class="button" href="%s">Send Mail </a>' % button_url)

    send_mail_button.short_description = "Student Sent Mail"


   

class GuardianAdmin(admin.ModelAdmin):
    model = Guardian
    list_display = ['id','first_name', 'last_name', 'student', 'relation', 'address', 'mobile_number']


admin.site.register(Student, StudentAdmin)
admin.site.register(Guardian, GuardianAdmin)
