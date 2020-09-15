from django.shortcuts import render
from django.http import HttpResponse
from main_app import forms
from django.contrib import messages
# Create your views here.

def home(request):

    if request.method == 'POST':
        data = request.POST.copy()
        form = forms.ContactForm(data)
        if form.is_valid():
            form.save()
            response = HttpResponse("OK")
            response.status_code = 200
            return response
        else:
            response = HttpResponse()
            response.status_code = 400
            return response

    return render(request, "home.html")
