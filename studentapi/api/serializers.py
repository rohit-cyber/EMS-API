from rest_framework import serializers
from .models import Student,Guardian



# Student serializer class

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','first_name','last_name','email','standard','evaluation','city','country','active','joined_on')


# Guardian serializer class

class GuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardian
        fields = ('id','first_name','last_name','relation','address','mobile_number')


# StudentWithGuardian serializer class
class StudentWithGuardianSerializer(serializers.ModelSerializer):
    guardians = GuardianSerializer(many=True)
    class Meta:
        model = Student
        fields = ('id','first_name','last_name','email','guardians','standard','evaluation','city','country','active','joined_on')
    
    def create(self, validated_data):
        guardians_data = validated_data.pop('guardians')
        student = Student.objects.create(**validated_data)
        for guardian_data in guardians_data:
            Guardian.objects.create(student=student, **guardian_data)
        return student