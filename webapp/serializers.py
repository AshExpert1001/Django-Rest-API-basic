from rest_framework import serializers
from .models import Employees, questions

class EmployeesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employees
        # fields = ('emp_name','emp_phone')
        fields = '__all__'

class questionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = questions
        fields = '__all__'