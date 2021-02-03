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
