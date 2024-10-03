from django.shortcuts import render
from .models import ContactInfo

def home(request):
    contact_info = ContactInfo.objects.first()

    if contact_info:
        print("ContactInfo Details:")
        print("Name:", contact_info.name)
        print("Photo URL:", contact_info.photo.url if contact_info.photo else "No photo")
    else:
        print("No ContactInfo object found.")

    context = {
        'contact': contact_info
    }

    # Debugging statements
    print("ContactInfo:", contact_info)

    return render(request, 'portfolio/home.html', context)