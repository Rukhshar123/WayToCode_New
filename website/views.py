from django.shortcuts import render,redirect
from .models import *

def webindex(request):
    service = Service.objects.all
    possibility = MaximumPossibilities.objects.all
    review = Reviews.objects.all
    return render(request,'webindex.html',{'service':service,'possibility':possibility,'review':review})

def webabout(request):
    team = Team.objects.all
    port = Portfolio.objects.all
    return render(request,'webabout.html',{'team':team,'port':port})

def webDevelopment(request):
    web = Service.objects.filter(name='Web Development')
    #print(web)
    return render(request, 'webdevelopment.html',{'web':web})

def appDevelopment(request):
    app = Service.objects.filter(name='App Development')
    return render(request, 'appdevelopment.html',{'app':app})

def webDesigning(request):
    design = Service.objects.filter(name='Design Services')
    return render(request, 'designservices.html',{'design':design})

def digitalMarketing(request):
    marketing = Service.objects.filter(name='Digital Marketing')
    return render(request, 'digitalmarketing.html',{'marketing':marketing})

def testing(request):
    testing = Service.objects.filter(name='QA & Testing')
    return render(request, 'testing.html',{'testing':testing})

def portfolio(request):
    port = Portfolio.objects.all
    return render(request, 'portfolio.html',{'port':port})

def ceo(request):
    return render(request, 'ceo.html')

def career(request):
    career = Career.objects.all()
    return render(request, 'career.html',{'career':career})

def webcontact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['comments']

        obj = Contact(name=name,email=email,phone=phone,description=desc)
        obj.save()
        return redirect('webcontact')

    return render(request, 'webcontact.html')

def aspnetTechnology(request):
    asp = Technology.objects.filter(name='ASP .NET Development')
    return render(request, 'asp.net.html',{'asp':asp})

def pythonTechnology(request):
    python = Technology.objects.filter(name='Python Development')
    return render(request, 'python.html',{'python':python})

def javaTechnology(request):
    java = Technology.objects.filter(name='Java Development')
    return render(request, 'java.html',{'java':java})

def phpTechnology(request):
    php = Technology.objects.filter(name='PHP Development')
    return render(request, 'php.html',{'php':php})

def androidTechnology(request):
    android = Technology.objects.filter(name='Android Development')
    return render(request, 'android.html',{'android':android})

def iosTechnology(request):
    ios = Technology.objects.filter(name='IOS Development')
    return render(request, 'ios.html',{'ios':ios})

def angularjsTechnology(request):
    angular = Technology.objects.filter(name='AngularJS Development')
    return render(request, 'angularjs.html',{'angular':angular})

def nodejsTechnology(request):
    node = Technology.objects.filter(name='NodeJS Development')
    return render(request, 'nodejs.html',{'node':node})

def reactjsTechnology(request):
    react = Technology.objects.filter(name='ReactJS Development')
    return render(request, 'reactjs.html',{'react':react})

def rorTechnology(request):
    ror = Technology.objects.filter(name='Ruby On Rails Development')
    return render(request, 'ror.html',{'ror':ror})

def golangTechnology(request):
    golang = Technology.objects.filter(name='GOLANG Development')
    return render(request, 'golang.html',{'golang':golang})

