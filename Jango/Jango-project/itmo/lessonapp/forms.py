from django import forms
from .models import Student, Lesson


class AttendanceForm(forms.Form):
    student = forms.ModelChoiceField(queryset=Student.objects.all())
    lesson = forms.ModelChoiceField(queryset=Lesson.objects.all())



class EnterForm(forms.Form):
    login = forms.CharField(label='login', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class RegForm(forms.Form):
    login = forms.CharField(label='login', max_length=100)
    password = forms.CharField(label='password', max_length=100)
    first_name = forms.CharField(label='first_name', max_length=100)
    last_name = forms.CharField(label='last_name', max_length=100)
    email = forms.CharField(label='email', max_length=100)