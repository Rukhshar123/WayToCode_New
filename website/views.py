from django.shortcuts import render

def webindex(request):
    return render(request,'webindex.html')

def webabout(request):
    return render(request,'webabout.html')

def webDevelopment(request):
    return render(request, 'webdevelopment.html')

def appDevelopment(request):
    return render(request, 'appdevelopment.html')

def webDesigning(request):
    return render(request, 'designservices.html')

def digitalMarketing(request):
    return render(request, 'digitalmarketing.html')

def testing(request):
    return render(request, 'testing.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def ceo(request):
    return render(request, 'ceo.html')

def career(request):
    return render(request, 'career.html')

def webcontact(request):
    return render(request, 'webcontact.html')

def aspnetTechnology(request):
    return render(request, 'asp.net.html')

def pythonTechnology(request):
    return render(request, 'python.html')

def javaTechnology(request):
    return render(request, 'java.html')

def phpTechnology(request):
    return render(request, 'php.html')

def androidTechnology(request):
    return render(request, 'android.html')

def iosTechnology(request):
    return render(request, 'ios.html')

def angularjsTechnology(request):
    return render(request, 'angularjs.html')

def nodejsTechnology(request):
    return render(request, 'nodejs.html')

def reactjsTechnology(request):
    return render(request, 'reactjs.html')

def rorTechnology(request):
    return render(request, 'ror.html')

def golangTechnology(request):
    return render(request, 'golang.html')

