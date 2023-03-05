from django.shortcuts import render, redirect
from .forms import SignUp, LoginForm, UploadDocument, announcmentform, StudentEmailForm, parentemailform
from django.contrib.auth import authenticate, login
from .models import StudentData, uploaddata, StudentData1, Announcements1,Student, Parent
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            emil = data['email']
            user = form.save()
            msg = 'user created'
            return redirect('loginpage')
        else:
            msg = 'form is invalid'
    else:
        form = SignUp()
    return render(request,'register.html',{'form': form, 'msg': msg})


def loginpage(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('home')
            elif user is not None and user.is_student:
                login(request, user)
                return redirect('studenthome')
            elif user is not None and user.is_staff:
                login(request, user)
                return redirect('staffhome')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validing form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def home(request):
    return render(request, 'homepage.html')


def students(request):
    temp = Announcements1.objects.all().order_by('-date')[:5]
    up = uploaddata.objects.all().order_by('-id')
    currnet_user = request.user
    cu = currnet_user.username
    if request.method == 'POST':
        fm = UploadDocument(request.POST)
        if fm.is_valid():
            rno = fm.cleaned_data.get('regno')
            sub = fm.cleaned_data.get('subject')
            lnk = fm.cleaned_data.get('link')
            sav = uploaddata(subject=sub,regno=rno,link=lnk)
            sav.save()
            fm = UploadDocument()
    else:
        fm = UploadDocument()

    return render(request, 'students.html',{'form':fm,'up':up ,'cu':cu, 't':temp})


def staff(request):
    if request.method == 'GET':
        t = request.GET.get('search',None)
        try:
            temp = uploaddata.objects.filter(regno__icontains=t).order_by('-id')
        except:
            temp = uploaddata.objects.all().order_by('-id')
    else:
        temp = uploaddata.objects.all().order_by('-id')
    
    return render(request, 'staff.html', {'up':temp})

def studentd(request):
    sd = StudentData1.objects.order_by('regno')
    return render(request, 'studentdata.html',{'sd':sd})

def calendar(request):
    return render(request,'calendar.html')

def attendence(request):
    currnet_user = request.user
    cu = currnet_user.username 
    msg = 'NO Found'
    sd = StudentData1.objects.all()
    sub = ['Software Engineering', 'Database Design']
    return render(request,'attendence.html',{'msg':msg, 'mo':sd, 'cu':cu, 'sub':sub})
        
def announce(request):
    temp = Announcements1.objects.all().order_by('-date')
    if request.method == 'POST':
        fm = announcmentform(request.POST)
        if fm.is_valid():
            sub = fm.cleaned_data.get('subject')
            tex = fm.cleaned_data.get('text')
            sav = Announcements1(subject=sub,text=tex)
            sav.save()
    else:
        fm = announcmentform()
    return render(request,'staffann.html', {'t':temp, 'form':fm})

def stannounce(request):
    temp = Announcements1.objects.all().order_by('-date')
    return render(request, 'studentannouncements.html' , {'t':temp})

def studentmail(request):
    if request.method == 'POST':
        form = StudentEmailForm(request.POST)
        if form.is_valid():
            recipients = form.cleaned_data['recipients']
            recipient_emails = recipients.values_list('email', flat=True)
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            send_mail(
                subject,
                body,
                'shashanksj111222@gmail.com',
                recipient_emails,
                fail_silently=False,
            )
    else:
        form = StudentEmailForm()
    students = Student.objects.all()
    return render(request, 'sendmailstudents.html', {'form': form, 'students': students})

def parentmail(request):
    if request.method == 'POST':
        form = parentemailform(request.POST)
        if form.is_valid():
            recipients = form.cleaned_data['recipients']
            recipient_emails = recipients.values_list('email', flat=True)
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            send_mail(
                subject,
                body,
                'shashanksj111222@gmail.com',
                recipient_emails,
                fail_silently=False,
            )
    else:
        form = parentemailform()
    students = Parent.objects.all()
    return render(request,'parentemailform.html', {'form': form, 'students': students} )