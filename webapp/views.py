from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employees, questions
from .serializers import EmployeesSerializer, questionsSerializer

# Create your views here.
class empList(APIView):

    def get(self, request):
        emp=Employees.objects.all()
        serilizer = EmployeesSerializer(emp, many=True)
        return Response(serilizer.data)

    def post(self):
        pass

class questionlist(APIView):

    def get(self, request):
        qlist=questions.objects.all()
        serilizer = questionsSerializer(qlist, many=True)
        return Response(serilizer.data)

def home(request):
    return HttpResponse("<h1>Django Rest Framework Api</h1><br><p>Some Dummy Data here..</p> <br> <a href='/que'>Questions Api</a> <br> <a href='/emp'>Employee Api</a>")