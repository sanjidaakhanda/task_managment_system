from django.shortcuts import render,redirect
from . import forms

# Create your views here.
def task_person(request):
    if request.method == "POST":
         person_form = forms.PersonForm(request.POST)
         if person_form.is_valid():
            person_form.save()
            return redirect ('home')
    else:
        person_form = forms.PersonForm()

    return render(request,'task_person.html',{'form':person_form})




