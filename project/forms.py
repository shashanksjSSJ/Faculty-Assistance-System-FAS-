from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Student,Parent
class LoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                'style':'width: 400px; padding:4px; border-radius:10px'
            }
        )
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "class":"form-control",
                'style':'width: 400px; padding:4px; border-radius:10px'
            }
        )
    )

class SignUp(UserCreationForm):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                'style':'width: 400px; padding:4px; border-radius:10px; ; '
            }
        )
    )

    password1= forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                'style':'width: 180px; padding:4px; border-radius:10px'
            }
        )
    )
    password2= forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                'style':'width: 180px; padding:4px; border-radius:10px'
            }
        )
    )
    email = forms.CharField(
        widget = forms.EmailInput(
            attrs={
                "class": "form-control",
               'style':'width: 400px; padding:4px; border-radius:10px'
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2' , 'is_staff', 'is_student')



class UploadDocument(forms.Form):
    regno = forms.CharField(label='USN', widget=forms.TextInput(attrs={'placeholder': 'USN', 'style': 'width: 300px; color:gray; padding:2px; height:40px; background-color:white; border-radius: 10px; margin:4px;', 'class': 'form-control'}))
    subject = forms.CharField(label='Subject',widget=forms.TextInput(attrs={'placeholder': 'Subject', 'style': 'width:300px; color:gray; 300px; padding:2px; height:40px; background-color:white; border-radius: 10px; margin:4px;', 'class': 'form-control'}))
    link = forms.CharField(label='Drive Link',widget=forms.TextInput(attrs={'placeholder': 'Drive Link', 'style': 'width: 600px; color:gray; padding:2px; height:40px; background-color:white; border-radius: 10px; margin:4px;', 'class': 'form-control'}))


class announcmentform(forms.Form):
    subject = forms.CharField(label='Subject',widget=forms.TextInput(attrs={'placeholder': 'Subject', 'style': 'width:600px; color:gray; 300px; padding:2px; height:40px; background-color:white; border-radius: 10px; margin:4px;', 'class': 'form-control'}))
    text = forms.CharField(label='Subject',widget=forms.Textarea(attrs={'placeholder': 'Text', 'style': 'width:600px; height:300px; color:gray; 300px; padding:2px; height:40px; background-color:white; border-radius: 10px; margin:4px;', 'class': 'form-control'}))

class StudentEmailForm(forms.Form):
    recipients = forms.ModelMultipleChoiceField(
        queryset=Student.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    subject = forms.CharField(label='Subject',widget=forms.TextInput(attrs={'placeholder': 'Subject', 'style': 'width:600px; color:gray; 300px; padding:2px; height:40px; background-color:white; border-radius: 10px; margin:4px;', 'class': 'form-control'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Body', 'style': 'width:600px; color:gray; 300px; padding:2px; height:    ; background-color:white; border-radius: 10px; margin:4px;', 'class': 'form-control'}))

class parentemailform(forms.Form):
    recipients = forms.ModelMultipleChoiceField(
        queryset=Parent.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    subject = forms.CharField(label='Subject',widget=forms.TextInput(attrs={'placeholder': 'Subject', 'style': 'width:600px; color:gray; 300px; padding:2px; height:40px; background-color:white; border-radius: 10px; margin:4px;', 'class': 'form-control'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Body', 'style': 'width:600px; color:gray; 300px; padding:2px; height:    ; background-color:white; border-radius: 10px; margin:4px;', 'class': 'form-control'}))
