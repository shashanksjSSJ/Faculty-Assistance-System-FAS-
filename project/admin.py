from django.contrib import admin
from .models import User,StudentData, uploaddata,StudentData1, Announcements1, Student,Parent
# Register your models here.

admin.site.register(User)
admin.site.register(StudentData)
admin.site.register(uploaddata)
admin.site.register(StudentData1)
admin.site.register(Announcements1)
admin.site.register(Parent)
admin.site.register(Student)