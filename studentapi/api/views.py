from django.shortcuts import render
from .serializers import StudentWithGuardianSerializer, StudentSerializer, GuardianSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student,Guardian
from datetime import date
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication



class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


#  Add Student API

class AddStudentAPI(APIView):

    serializer_class = StudentSerializer

    def post(self,request,format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'student data added'})


#  Add Guardian API

class AddGuardianAPI(APIView):

    serializer_class = GuardianSerializer

    def post(self,request,format=None):
        serializer = GuardianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Guardian data added'})


# list all StudentWithGuardian API

class StudentWithGuardianAPI(APIView):

    serializer_class = StudentWithGuardianSerializer
    permission_classes=[ IsAuthenticated ]

    def get(self,request,format=None):
        student = Student.objects.all()
        serializer = StudentWithGuardianSerializer(student,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = StudentWithGuardianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data added'})
        return Response(serializer.errors)




# return all active students API

class ActiveStudentsAPI(APIView):

    serializer_class = StudentSerializer

    def get(self,request,format=None):
        active_student = Student.objects.filter(active=True)
        serializer = StudentSerializer(active_student,many=True)
        return Response(serializer.data)


# return all pass students API

class EvalStudentAPI(APIView):

    serializer_class = StudentSerializer
    

    def post(self,request,format=None):
        get_data = request.query_params
        eval_student = Student.objects.filter(evaluation=get_data['evaluation'])
        serializer = StudentSerializer(eval_student,many=True)
        return Response(serializer.data)


# return all student who joined this year API

class JoinDateStudentAPI(APIView):

    serializer_class = StudentSerializer
    
    def get(self,request,format=None):
        today = date.today()
        date_student = Student.objects.filter(joined_on__year=today.year)
        serializer = StudentSerializer(date_student,many=True)
        return Response(serializer.data)

class SortStudentAPI(APIView):

    serializer_class = StudentSerializer

    def get(self,request,format=None):
        sort_student = Student.objects.order_by('first_name')
        serializer = StudentSerializer(sort_student,many=True)
        return Response(serializer.data)


# student Detail and Delete API

class StudentDetailDeleteAPI(APIView):
    
    serializer_class = StudentSerializer
    
    def get(self,request,pk=None,format=None):
        if pk is not None:
            try:
                student = Student.objects.get(id=pk)
                serializer = StudentSerializer(student)
                return Response(serializer.data)
            except:
                return Response({'msg':'Enter valid id'})
        else:
            student = Student.objects.all()
            serializer = StudentSerializer(student,many=True)
            return Response(serializer.data)


    def delete(self,request,pk,format=None):
        student = Student.objects.get(id=pk)
        student.delete()
        return Response({'msg':'Student data Deleted'})



class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = ['evaluation']
    ordering_fields = ['first_name','last_name']


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

class LogoutView(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def post(self,request):
        logout(request)
        return Response({'msg':'logged Out'},status=status.HTTP_200_OK)




  



