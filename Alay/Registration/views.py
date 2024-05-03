from django.shortcuts import render
from django import forms
# Create your views here.

class Form(forms.Form):
    Form = forms.CharField(label="Login")
def index(request):
    return render(request, 'Registration/index.html',{
        'form':Form
    })