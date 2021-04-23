from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from .serializers import RegisterSerializer,ProfileSerializer
from myapp.models import Profile
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.views.decorators.csrf import csrf_protect
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening




class ProfileAPI(APIView):

    serializer_class = ProfileSerializer
    permission_classes=[ AllowAny ]
    
    def get(self,request, format=None):

        id = request.query_params.get('id')

        if id is not None:
            try:
                profile = Profile.objects.get(id=id)
                serializer = ProfileSerializer(profile)
                return Response(serializer.data,status = status.HTTP_200_OK)
            except:
                return Response({'msg':"Enter a valid Id"},status=status.HTTP_406_NOT_ACCEPTABLE)
        
        else:
            profile = Profile.objects.all()
            serializer = ProfileSerializer(profile,many=True)
            return Response(serializer.data,status = status.HTTP_200_OK)

    def post(self,request,format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def put(self,request,format = None):
        id = request.query_params.get('id')
        profile = Profile.objects.get(id=id)
        serializer = ProfileSerializer(profile, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete data updated'} ,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def delete(self,request,format=None):
        id = request.query_params.get('id')
        profile=Profile.objects.get(id=id)
        profile.delete()
        return Response({'msg':'Data Deleted'},status = status.HTTP_200_OK)


class LoginApiView(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def post(self,request,format=None,**kwargs):

        username=request.query_params.get('username')
        password=request.query_params.get('password')

        user=authenticate(username=username,password=password)
        if user is None:
            return Response({'msg':'User not found'},status=status.HTTP_401_UNAUTHORIZED)
        else:
            login(request, user)
            return Response({'msg':'User logged in'},status=status.HTTP_200_OK)


class RegistrationAPI(APIView):
     
    serializer_class = RegisterSerializer
    permission_classes=[ IsAuthenticated ]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get(self,request, format=None):

        id = request.query_params.get('id')

        if id is not None:
            try:
                register = User.objects.get(id=id)
                serializer = RegisterSerializer(register)
                return Response(serializer.data,status = status.HTTP_200_OK)
            except:
                return Response({'msg':"Enter a valid Id"},status=status.HTTP_406_NOT_ACCEPTABLE)
        
        else:
            register = User.objects.all()
            serializer = RegisterSerializer(register,many=True)
            return Response(serializer.data,status = status.HTTP_200_OK)


    def post(self,request,format=None):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'User Registered'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def post(self,request):
        logout(request)
        return Response({'msg':'logged Out'},status=status.HTTP_200_OK)




    



    

