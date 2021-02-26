from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    training = Training.objects.all()
    review = StudentReview.objects.all()
    blog = Blog.objects.all()
    return render(request,'index.html',{'training':training,'review':review,'blog':blog})

def about(request):
    return render(request,'about.html')

def liveTraining(request):
    live = Training.objects.filter(name='Live Training')
    technology = TrainingTechnology.objects.all()
    return render(request,'live_training.html',{'live':live,'technology':technology})

def collegeInternship(request):
    college = Training.objects.filter(name='College Internship')
    technology = TrainingTechnology.objects.all()
    return render(request,'college_internship.html',{'college':college,'technology':technology})

def collegeProject(request):
    project = Training.objects.filter(name='College Project')
    technology = TrainingTechnology.objects.all()
    return render(request,'college_project.html',{'project':project,'technology':technology})

def industrialTraining(request):
    industry = Training.objects.filter(name='Industrial Training')
    technology = TrainingTechnology.objects.all()
    return render(request,'industrial_training.html',{'industry':industry,'technology':technology})

def onlineTraining(request):
    online = Training.objects.filter(name='Online Training')
    technology = TrainingTechnology.objects.all()
    return render(request,'online_training.html',{'online':online,'technology':technology})

def joborientedTraining(request):
    job = Training.objects.filter(name='Job Oriented Training')
    technology = TrainingTechnology.objects.all()
    return render(request,'job-oriented_training.html',{'job':job,'technology':technology})

def contact(request):
    return render(request, 'contact.html')

def blogs(request):
    blog = Blog.objects.all()
    return render(request, 'blogs.html',{'blog':blog})

def webDevelopment(request):
    return render(request, 'web_development.html')

def appDevelopment(request):
    return render(request, 'app_development.html')

def digitalMarketing(request):
    return render(request, 'digital_marketing.html')

def webDesigning(request):
    return render(request, 'web_designing.html')

def softwareTesting(request):
    return render(request, 'software_testing.html')

def advanceCourse(request):
    return render(request, 'advance_courses.html')

def trainingPhp(request):
    return render(request,'trainingphp.html')

def trainingASP(request):
    return render(request, 'trainingasp.html')

def trainingJava(request):
    return render(request, 'trainingjava.html')

def trainingPython(request):
    return render(request, 'trainingpython.html')

def trainingROR(request):
    return render(request, 'trainingror.html')

def trainingGolang(request):
    return render(request, 'traininggolang.html')

def trainingAndroid(request):
    return render(request, 'trainingandroid.html')

def trainingIos(request):
    return render(request, 'trainingios.html')

def trainingFlutter(request):
    return render(request, 'trainingflutter.html')

def trainingSEO(request):
    return render(request, 'seo.html')

def trainingMarketing(request):
    return render(request, 'digimarketing.html')

def trainingContent(request):
    return render(request, 'content.html')

def trainingUIUX(request):
    return render(request, 'uiux.html')

def trainingAngular(request):
    return render(request, 'angular.html')

def trainingReact(request):
    return render(request, 'react.html')

def trainingSofttesting(request):
    return render(request, 'softwaretesting.html')

def trainingManuelTesting(request):
    return render(request, 'manueltesting.html')

def trainingAutoTesting(request):
    return render(request, 'automationtesting.html')

def trainingAI(request):
    return render(request, 'ai.html')

def trainingML(request):
    return render(request, 'ml.html')

def trainingDataScience(request):
    return render(request, 'datascience.html')