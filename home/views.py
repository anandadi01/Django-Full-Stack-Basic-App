from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, HttpResponse
from home.models import Contact
from datetime import datetime

from django.contrib import messages

# Create your views here.

def index(request):

    context={
        'variable1': "aditya is a good boy",
        'variable2': "amisha and drishti are good girls",
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is the HomePage")   
def about(request):
    # return HttpResponse("This is the About Page"),
    return render(request, 'about.html')

def services(request):
    # return HttpResponse("This is the Services Page"),
    return render(request, 'services.html')

def contact(request):
    # return HttpResponse("This is the Contacts Page"),
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        print(name, email)


        contact = Contact(name= name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent.')

    return render(request, 'contact.html')
