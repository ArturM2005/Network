from django.shortcuts import render
from django import forms
# Create your views here.

class Forms(forms.Form):
    Reg = forms.CharField(label="Login")
def index(request):
    if request.method == 'POST':
        form = Forms(request.POST)
        if form.is_valid():
            Reg = form.cleaned_data["Reg"]
    return render(request, 'Registration/index.html',{
        'form':Forms
    })