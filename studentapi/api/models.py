from django.db import models

# Create your models here.

# Student Table

class Student(models.Model):

    STD_CHOICES = (('one','One'),
               ('two','Two'),
               ('three','Three'),
               ('four','Four'),
               ('five','Five'),
               ('six','Six'),
               ('seven','Seven'),
               ('eight','Eight'),
               ('nine','Nine'),
               ('ten','Ten'),
              )


    EVALUATION_CHOICES = (('pass','Pass'),
                      ('fail','Fail'),
                      )

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


# Guardian Table

class Guardian(models.Model):

    RELATION_CHOICES = (('father','Father'),
                    ('mother','Mother'),
                    ('other','Other'),
                    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student = models.ForeignKey(Student, related_name='guardians', on_delete=models.CASCADE)
    relation = models.CharField(choices=RELATION_CHOICES,max_length=50)
    address = models.TextField(blank=True)
    mobile_number = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name



