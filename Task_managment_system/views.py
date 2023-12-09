from django.shortcuts import render
from task_app.models import Task

def home(request):
    data = Task.objects.all()
    return render (request,'home.html',{'data':data})