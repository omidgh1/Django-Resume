from django.shortcuts import render
from .models import Logo, ContactInfo

def home(request):
    logo = Logo.objects.first()
    contact = ContactInfo.objects.first()

    if contact:
        print("ContactInfo Details:")
        print("Name:", contact.name)
        print("Phone:", contact.phone)
        print("Email:", contact.email)
        print("Photo URL:", contact.photo.url if contact.photo else "No photo")
    else:
        print("No ContactInfo object found.")

    context = {
        'logo': logo,
        'contact': contact
    }

    # Debugging statements
    print("Logo:", logo)
    print("ContactInfo:", contact)

    return render(request, 'portfolio/home.html', context)