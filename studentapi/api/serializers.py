from rest_framework import serializers
from .models import Student,Guardian



# Student serializer class

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('first_name','last_name','standard','evaluation','city','country','active','joined_on')


# Guardian serializer class

class GuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardian
        fields = ('first_name','last_name','student','relation','address','mobile_number')


# StudentWithGuardian serializer class
class StudentWithGuardianSerializer(serializers.ModelSerializer):
    guardians = GuardianSerializer(many=True, read_only=True)
    class Meta:
        model = Student
        fields = ('first_name','last_name','guardians','standard','evaluation','city','country','active','joined_on')