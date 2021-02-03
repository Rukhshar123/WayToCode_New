"""waytocode URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from training import views as training
from website import views as web

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',web.webindex,name="webindex"),
    path('about',web.webabout,name="about"),
    path('webdevelopment',web.webDevelopment,name="webdevelopment"),
    path('appdevelopment',web.appDevelopment,name="appdevelopment"),
    path('webdesigning',web.webDesigning,name="webdesigning"),
    path('digitalmarketing',web.digitalMarketing,name="digitalmarketing"),
    path('testing',web.testing,name="testing"),
    path('portfolio',web.portfolio,name="portfolio"),

    #Training URLs
    path('index',training.index,name="index"),
    path('about_training',training.about,name="about_training"),
    path('livetraining',training.liveTraining,name="livetraining"),
    path('collegeinternship',training.collegeInternship,name="collegeinternship"),
    path('collegeproject',training.collegeProject,name="collegeproject"),
    path('industrialtraining',training.industrialTraining,name="industrialtraining"),
    path('onlinetraining',training.onlineTraining,name="onlinetraining"),
    path('joboriented',training.joborientedTraining,name="joboriented"),
    path('contact',training.contact,name="contact"),

]
