from django.core.mail import send_mail
from .models import Table

def send_email_to_customers():
    customers = Table.objects.all()
    for customer in customers:
        send_mail(
            subject='Thank you for being with us!',
            message=f'Hello {customer.name}, we appreciate your support.',
            from_email='urbandev017@gmail.com',
            recipient_list=[customer.email],
            fail_silently=False,
        )