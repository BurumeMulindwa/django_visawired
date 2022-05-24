import random
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

from vwired.models import Contact


def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def services(request):
    return render(request, 'services.html', {})


def prices(request):
    return render(request, 'prices.html', {})


def pay_fast(request):
    return render(request, 'pay_fast.html', {})


def contact_landing(request):
    return render(request, 'contact_landing.html', {})


num = random.randrange(1021, 9899)
str_num = str(num)


def contact_captcha(request):
    # num = random.randrange(1001, 9999)
    global str_num
    str_num = str(num)
    return render(request, "contact.html", {"cap": str_num})


def contact(request):
    if request.method == 'POST':
        first_name = request.POST['FirstName']
        last_name = request.POST['LastName']
        passport_number = request.POST['PassportNumber']
        date_of_birth = request.POST['DateOfBirth']
        email = request.POST['Email']
        phone_number = request.POST['PhoneNumber']
        brief_description = request.POST['BriefDescription']
        captcha = request.POST.get('cap')

        new_contact = Contact(first_name=first_name, last_name=last_name, passport_number=passport_number,
                              date_of_birth=date_of_birth, email=email, phone_number=phone_number,
                              brief_description=brief_description)

        new_contact.save()

        if str_num == str(captcha):
            # send an email
            send_mail(
                'Message from ' + first_name + ' ' + last_name,  # subject
                brief_description + ' written by ' + email,  # message
                email,  # from email
                ['deziburume@gmail.com'],  # to email
            )
            return HttpResponse("<h4>YOUR FORM HAS BEEN SUBMITTED SUCCESSFULLY</h4>")
        else:
            return HttpResponse("<h4>CAPTCHA NOT MATCHED!!!</h4>")
    else:
        return HttpResponse("<h4>SERVER ERROR</h4>")
