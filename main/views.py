from django.http import HttpResponse
from django.shortcuts import render
from .models import Department, Chef, Occasion, Testimonies, MenuType, Menu, Table, Contact
from .utils import send_email_to_customers

def email_customers(request):
    send_email_to_customers()
    return HttpResponse("Emails sent!")

def home(request):
    if request.method  == 'POST':
        form_type = request.POST.get("form_type")
        if form_type == 'table':
            name = request.POST.get("name")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            date = request.POST.get("date")
            time = request.POST.get("time")
            number = request.POST.get("people")
            message = request.POST.get("message")
            table = Table()
            table.name = name
            table.email = email
            table.phone = phone
            table.date = date + ' ' + time
            table.message = message
            print(date + time)
            table.save()
        if form_type == 'contact':
            name = request.POST.get("name")
            email = request.POST.get("email")
            subject = request.POST.get("subject")
            message = request.POST.get("message")
            contact = Contact()
            contact.name = name
            contact.email = email
            contact.subject = subject
            contact.message = message
            contact.save()
    context = {
        'menu': Menu.objects.all(),
        'occasion': Occasion.objects.all(),
        'chef': Chef.objects.all(),
        'testi': Testimonies.objects.all()
        
    }
    return render(request, 'index.html', context=context)
# Create your views here.
