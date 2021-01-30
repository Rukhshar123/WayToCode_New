from django.shortcuts import render

def webindex(request):
    return render(request,'webindex.html')
