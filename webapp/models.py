from django.db import models

# Create your models here.

class Employees(models.Model):
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length=25)
    emp_phone = models.CharField(max_length=10)

    def __str__(self):
        return self.emp_name

class questions(models.Model):
    question = models.CharField(max_length=150)
    choice1 = models.CharField(max_length=50)
    choice2 = models.CharField(max_length=50)
    choice3 = models.CharField(max_length=50)
    choice4 = models.CharField(max_length=50, default="")
    answer = models.IntegerField()

    def __str__(self):
        return self.question