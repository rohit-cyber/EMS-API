from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display=['id','name','city','gender']


admin.site.register(Profile,ProfileAdmin)

