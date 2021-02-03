from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def liveTraining(request):
    return render(request,'live_training.html')

def collegeInternship(request):
    return render(request,'college_internship.html')

def collegeProject(request):
    return render(request,'college_project.html')

def industrialTraining(request):
    return render(request,'industrial_training.html')

def onlineTraining(request):
    return render(request,'online_training.html')

def joborientedTraining(request):
    return render(request,'online_training.html')

def contact(request):
    return render(request, 'contact.html')

