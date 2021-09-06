from django.shortcuts import render

# Create your views here.
from .models import Contacts

from django.contrib import messages
from django.core.mail import send_mail

from django.conf import settings

def contact(request):
    if request.method =='POST':
        firstName=request.POST['name']
        lastName=request.POST['lname']
        business_fields=request.POST['business_field']
        phone=request.POST['phone']
        email=request.POST['email']
        message=request.POST['message']
        send_mail(
            '@spsk',
            'YOUR FORM WAS SUBMITTED  please call +91 8955383802',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        if len(firstName) < 2 or len(lastName) < 4 or len(business_fields) < 5 or len(email) < 10 or len(phone) < 10 or len(message) < 10:
            messages.error(request,'PLEASE FILL FORM CORRECTLY')
        else:
            contact=Contacts(firstName=firstName,lastName=lastName,business_field=business_fields,phone=phone,email=email,message=message)
            contact.save()
            messages.success(request, 'YOUR FORM HAVE BEEN SUBMITTED PLEASE CHECK YOUR EMAIL')
    return render(request,'tlcs/contact.html')




def home(request):
    return render(request,'tlcs/home.html')

def services(request):
    return render(request,'tlcs/services.html')

def services_2(request):
    return render(request,'tlcs/services_2.html')

def team(request):
    return render(request,'tlcs/team.html')

def project_one(request):
    return render(request,'tlcs/project_one.html')

def project_two(request):
    return render(request,'tlcs/project_two.html')

def web_one(request):
    return render(request,'tlcs/web_one.html')