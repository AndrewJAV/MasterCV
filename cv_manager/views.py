from django.shortcuts import render, get_object_or_404
from .models import *

def cv_detail(request,slug):
    person = get_object_or_404(Person, slug=slug)
    contacts = Contact.objects.filter(person=person)
    languages = Language.objects.filter(person=person)
    aptitudes = Aptitude.objects.filter(person=person)
    skills = Skill.objects.filter(person=person)
    educations = Education.objects.filter(person=person).order_by('-start_year')
    laboral_exp = LaboralExp.objects.filter(person=person)
    
    context = {
        'person':person,
        'contacts':contacts,
        'languages':languages,
        'aptitudes':aptitudes,
        'skills':skills,
        'educations':educations,
        'laboral_exp':laboral_exp,
    }
    return render(request,'cv.html',context)

# Create your views here.
