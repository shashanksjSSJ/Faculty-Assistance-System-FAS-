from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginpage, name='loginpage'), 
    path('register/',views.register,name='register'),
    path('home/', views.home, name='home'),
    path('studenthomepage/', views.students, name='studenthome'),
    path('staffhomepage/', views.staff,name='staffhome'),
    path('studentdata/',views.studentd,name='studentdata'),
    path('calendar/',views.calendar,name='calendar'),
    path('attendence/', views.attendence,name='attendence'),
    path('announcements/', views.announce,name='announce'),
    path('studentannouncements/', views.stannounce,name='stannounce'),
    path('studentmail/', views.studentmail, name='studentmail'),
    path('parentmail/', views.parentmail, name='parentmail'),
]