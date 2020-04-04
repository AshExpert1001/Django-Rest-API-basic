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