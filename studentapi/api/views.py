from django.shortcuts import render
from .serializers import StudentWithGuardianSerializer, StudentSerializer, GuardianSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student,Guardian
from datetime import date

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

    def get(self,request,format=None):
        student = Student.objects.all()
        serializer = StudentWithGuardianSerializer(student,many=True)
        return Response(serializer.data)


# return all active students API

class ActiveStudentsAPI(APIView):

    serializer_class = StudentSerializer

    def get(self,request,format=None):
        active_student = Student.objects.filter(active=True)
        serializer = StudentSerializer(active_student,many=True)
        return Response(serializer.data)

# return all student who joined this year API

class JoinDateStudentAPI(APIView):

    serializer_class = StudentSerializer
    
    def get(self,request,format=None):
        today = date.today()
        date_student = Student.objects.filter(joined_on__year=today.year)
        serializer = StudentSerializer(date_student,many=True)
        return Response(serializer.data)

  



