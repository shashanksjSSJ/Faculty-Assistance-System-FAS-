from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField('is admin',default=False)
    is_staff = models.BooleanField('is staff',default=False)
    is_student = models.BooleanField('is student',default=False)

class StudentData(models.Model):
    name = models.CharField(max_length=200)
    regno = models.CharField(max_length=10)
    parentname = models.CharField(max_length=200)
    emailid = models.EmailField(max_length=200)
    parentemail = models.EmailField(max_length=200)
    contact = models.CharField(max_length=10)
    studentcg = models.CharField(max_length=4)

    def __str__(self):
        return self.name

class StudentData1(models.Model):
    name = models.CharField(max_length=200)
    regno = models.CharField(max_length=10)
    parentname = models.CharField(max_length=200)
    emailid = models.EmailField(max_length=200)
    parentemail = models.EmailField(max_length=200)
    contact = models.CharField(max_length=10)
    studentcg = models.CharField(max_length=4)
    total1 = models.IntegerField()
    sub1 = models.IntegerField()
    total2 = models.IntegerField()
    sub2 = models.IntegerField()
    total3 = models.IntegerField()
    sub3 = models.IntegerField()
    total4 = models.IntegerField()
    sub4 = models.IntegerField()

    def __str__(self):
        return self.name


class uploaddata(models.Model):
    subject = models.CharField(max_length=100)
    regno = models.CharField(max_length=10)
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.subject

    
class Announcements1(models.Model):
    subject = models.CharField(max_length=100)
    text = models.TextField(max_length=10000)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.subject
    

class Student(models.Model):
    name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return f"{self.name} ({self.email}) USN: {self.reg_no}"

class Parent(models.Model):
    name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    studentname = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}, Ward name: {self.studentname}, Ward USN: {self.reg_no}, Eamil: {self.email}"