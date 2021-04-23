from django.contrib.auth.models import User
from rest_framework import serializers
from myapp.models import Profile

class RegisterSerializer(serializers.ModelSerializer):

    password=serializers.CharField(max_length=150,write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')

    def validate(self,args):
        return super().validate(args)

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'name' ,'city', 'gender')

