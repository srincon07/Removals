import pdb

# Django
from django.shortcuts import render
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist

# Services
from .models import Service_type, Service_item

# Clients
from clients.models import Client

# Inventory
from inventory.models import Furniture_type, Furniture_item

# Forms
from .forms import ServiceForm
from clients.forms import ClientForm, ContactForm


def clientExist(email):
    """ Validate if the customer info is already in the database

    return client

    """

    try:
        client = Client.objects.get(email=email)
    except ObjectDoesNotExist:
        return False

    return client


def sendServiceEmail(client, service, furniture):
    inv = [k + ' = ' + v for k, v in furniture.items()]

    # Send email requesting service
    subject = 'New removal requested'
    sender = client['email']
    message = client['name'] + ' has requested a new removal quote.' + '\n\n' + 'The following is the service information:\n\n' + \
        'Phone number: ' + client['phoneNumber'] + '\n' + \
        'Email: ' + sender + '\n' + \
        'Move date: ' + str(service['date']) + '\n' + \
        'Pick-up: ' + service['pickUp'] + '\n' + \
        'Pick-up Comments: ' + service['pickUpComment'] + '\n' + \
        'Drop-off: ' + service['dropOff'] + '\n' + \
        'Drop-off Comments: ' + service['dropOffComment'] + '\n' + \
        'Move type: ' + str(service['move']) + '\n' + \
        'Service type: ' + str(service['type']) + '\n\n' + \
        'Inventory: ' + '\n' + '\n'.join(inv)
    recipients = ['hello@nationwidemovers.com.au']

    send_mail(subject, message, sender, recipients)


def sendContactEmail(contact):
    subject = 'Message from Nationwidemovers.com.au'
    sender = contact['contact_sender']
    message = contact['contact_name'] + ' just sent the following message:' + '\n\n' + \
        contact['contact_message'] + '\n\n' + \
        'These are the contact details: \n' + sender + \
        '\n' + contact['contact_phoneNumber']

    recipients = ['hello@nationwidemovers.com.au']

    send_mail(subject, message, sender, recipients)


def booking_service(request):
    alert = {'success': ''}
    success_message = ''

    # Fetch furniture types and items
    furniture_type = Furniture_type.objects.all()
    furniture_item = Furniture_item.objects.all()

    if request.method == 'POST':
        formService = ServiceForm(request.POST)
        formClient = ClientForm(request.POST)
        form = ContactForm(request.POST)
        # pdb.set_trace()

        if 'contact_sender' not in request.POST:
            if formService.is_valid() and formClient.is_valid():
                # Get cleaned data from the form
                clientForm = formClient.cleaned_data
                serviceForm = formService.cleaned_data

                # Save customer
                client = clientExist(clientForm['email'])
                if client:
                    client.name = clientForm['name']
                    client.phoneNumber = clientForm['phoneNumber']
                    client.save()
                else:
                    formClient.save()

                new_service = formService.save(commit=False)
                new_service.clientId = Client.objects.get(
                    email=clientForm['email'])
                new_service.save()

                # Dict for the service inventory
                inventory = dict()

                for f_item in furniture_item:
                    quantity = request.POST[f_item.name]
                    if int(quantity) > 0:
                        Service_item.objects.create(
                            item=f_item, service=new_service, quantity=quantity)
                        inventory[f_item.name] = quantity

                sendServiceEmail(clientForm, serviceForm, inventory)
                alert['success'] = 'Thanks for reach us. We\'ll contact you soon.'
        else:
            if form.is_valid():
                contactForm = form.cleaned_data
                sendContactEmail(contactForm)
                success_message = 'Thanks for reach us. We\'ll contact you soon.'

    formService = ServiceForm()
    formClient = ClientForm()
    form = ContactForm()

    # Get service type conditions
    serviceTypes = Service_type.objects.all()
    types = [type for type in serviceTypes]

    return render(request, './services/service_form.html', {
        'formService': formService,
        'formClient': formClient,
        'alertSuccess': alert['success'],
        'furnitureTypes': furniture_type,
        'furnitureItems': furniture_item,
        'serviceTypes': types,
        'contactForm': form,
        'success': success_message
    })
