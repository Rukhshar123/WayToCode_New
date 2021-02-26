from django.contrib import admin
from django.urls import path
from website import views as web
from django.conf.urls.static import static
from django.conf import settings

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
    path('ceo',web.ceo,name="ceo"),
    path('career',web.career,name="career"),
    path('webcontact',web.webcontact,name="webcontact"),
    path('webasp.net',web.aspnetTechnology,name="webasp.net"),
    path('webpython',web.pythonTechnology,name="webpython"),
    path('webjava',web.javaTechnology,name="webjava"),
    path('webphp',web.phpTechnology,name="webphp"),
    path('webandroid',web.androidTechnology,name="webandroid"),
    path('webios',web.iosTechnology,name="webios"),
    path('webangularjs',web.angularjsTechnology,name="webangularjs"),
    path('webnodejs',web.nodejsTechnology,name="webnodejs"),
    path('webreactjs',web.reactjsTechnology,name="webreactjs"),
    path('webror',web.rorTechnology,name="webror"),
    path('webgolang',web.golangTechnology,name="webgolang"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
