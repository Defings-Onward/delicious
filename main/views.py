from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Department, Chef, Occasion, Testimonies, MenuType, Menu, Table, Contact
from .utils import send_email_to_customers
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required

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
            table.read = False
            print(date + time)
            table.save()
            return redirect('/')
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
            return redirect('/')
        if form_type == 'signup':
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            password = request.POST.get("password")
            username = request.POST.get("username")
            user = User()
            user.username = username
            user.first_name = first_name
            user.last_name = last_name
            user.password = password
            user.save()
            login(request, user)
            print("signed in")
            #good
            return redirect('/')
        if form_type == 'event':
            photo = request.FILES.get('photo')
            title = request.POST.get('title')
            price = request.POST.get('price')
            p1 = request.POST.get('1p')
            b1 = request.POST.get('1b')
            b2 = request.POST.get('2b')
            b3 = request.POST.get('3b')
            p2 = request.POST.get('1p')
            occation = Occasion()
            occation.picture = photo
            occation.head  = title
            occation.price = price
            occation.para1 = p1
            occation.dot1 = b1
            occation.dot2 = b2
            occation.dot3 = b3
            occation.para2 = p2
            occation.save()
            return redirect('/')
        if form_type == 'menu':
            photo = request.FILES.get('photo')
            title = request.POST.get('title')
            price = request.POST.get('price')
            description = request.POST.get('description')
            type = request.POST.get('type')
            menu = Menu()
            menu.name = title
            menu.price = price
            menu.image = photo
            menu.description = description
            types = MenuType.objects.get(name=type)
            menu.type = types
            menu.save()
            return redirect('/')
        if form_type == 'unread':
            orders = Table.objects.filter(read=False)
            for order in orders:
                order.read = True
                order.save()
            return redirect('/#order')

    context = {
        'menu': Menu.objects.all(),
        'occasion': Occasion.objects.all(),
        'chef': Chef.objects.all(),
        'testimony': Testimonies.objects.all(),
        'table': Table.objects.all(),
        'unread': Table.objects.filter(read=False).count()
    }
    return render(request, 'index.html', context=context)
# Create your views here.
