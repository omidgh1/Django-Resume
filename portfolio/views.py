from django.shortcuts import render
from .models import ContactInfo, CVFile, Skills, Experience


def home(request):
    contact_info = ContactInfo.objects.first()
    cv_file = CVFile.objects.first()
    skills = Skills.objects.all()
    experiences = Experience.objects.all()

    # Preprocess skills to split by comma
    for skill in skills:
        skill.skills_list = [s.strip() for s in skill.skills.split(',')]

    for experience in experiences:
        experience.start_date_display = experience.get_start_date_display()
        experience.end_date_display = experience.get_end_date_display()

    context = {
        'contact': contact_info,
        'cvfile': cv_file,
        'skills': skills,
        'experiences': experiences
    }

    # Debugging statements
    print("ContactInfo:", contact_info)
    print("CVFile:", cv_file.file.url)
    print("Skills:", skills)
    print("Experiences:", experiences)

    return render(request, 'portfolio/home.html', context)
