from django.db import models

# Create your models here.

STD_CHOICES = (('One','One'),
               ('Two','Two'),
               ('Three','Three'),
               ('Four','Four'),
               ('Five','Five'),
               ('Six','Six'),
               ('Seven','Seven'),
               ('Eight','Eight'),
               ('Nine','Nine'),
               ('Ten','Ten'),
              )


EVALUATION_CHOICES = (('Pass','Pass'),
                      ('Fail','Fail'),
                      )

# Student Table

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    standard = models.CharField(choices=STD_CHOICES,max_length=50)
    evaluation = models.CharField(choices=EVALUATION_CHOICES,max_length=50)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    active = models.BooleanField(blank=True)
    joined_on = models.DateField(auto_now=False)

    def __str__(self):
        return self.first_name

RELATION_CHOICES = (('Father','Father'),
                    ('Mother','Mother'),
                    ('Other','Other'),
                    )

# Guardian Table

class Guardian(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student = models.ForeignKey(Student, related_name='guardians', on_delete=models.CASCADE)
    relation = models.CharField(choices=RELATION_CHOICES,max_length=50)
    address = models.TextField(blank=True)
    mobile_number = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name



