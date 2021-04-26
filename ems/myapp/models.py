from django.db import models
from django.contrib.auth.models import User


GENDER_CHOICES=(('Male','Male'),
                ('Female','Female'))


class Profile(models.Model):
    name=models.OneToOneField(User,on_delete=models.CASCADE)
    city=models.CharField(max_length=250)
    gender=models.CharField(choices=GENDER_CHOICES,max_length=250)
    

    def __str__(self):
        return str(self.name)


