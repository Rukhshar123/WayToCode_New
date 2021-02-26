
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',views.index,name="index"),
    path('about_training',views.about,name="about_training"),
    path('livetraining',views.liveTraining,name="livetraining"),
    path('collegeinternship',views.collegeInternship,name="collegeinternship"),
    path('collegeproject',views.collegeProject,name="collegeproject"),
    path('industrialtraining',views.industrialTraining,name="industrialtraining"),
    path('onlinetraining',views.onlineTraining,name="onlinetraining"),
    path('joboriented',views.joborientedTraining,name="joboriented"),
    path('contact',views.contact,name="contact"),
    path('blogs',views.blogs,name="blogs"),
    path('trainingwebdevelopment',views.webDevelopment,name="trainingwebdevelopment"),
    path('trainingappdevelopment',views.appDevelopment,name="trainingappdevelopment"),
    path('trainingdigimarketing',views.digitalMarketing,name="trainingdigimarketing"),
    path('trainingwebdesigning',views.webDesigning,name="trainingwebdesigning"),
    path('trainingtesting',views.softwareTesting,name="trainingtesting"),
    path('advancecourses',views.advanceCourse,name="advancecourses"),
    path('trainingphp',views.trainingPhp,name="trainingphp"),
    path('trainingasp',views.trainingASP,name="trainingasp"),
    path('trainingjava',views.trainingJava,name="trainingjava"),
    path('trainingpython',views.trainingPython,name="trainingpython"),
    path('trainingror',views.trainingROR,name="trainingror"),
    path('traininggolang',views.trainingGolang,name="traininggolang"),
    path('trainingandroid',views.trainingAndroid,name="trainingandroid"),
    path('trainingios',views.trainingIos,name="trainingios"),
    path('trainingflutter',views.trainingFlutter,name="trainingflutter"),
    path('trainingseo',views.trainingSEO,name="trainingseo"),
    path('trainingdigi',views.trainingMarketing,name="trainingdigi"),
    path('trainingcontent',views.trainingContent,name="trainingcontent"),
    path('trainingui',views.trainingUIUX,name="trainingui"),
    path('trainingangular',views.trainingAngular,name="trainingangular"),
    path('trainingreact',views.trainingReact,name="trainingreact"),
    path('trainingsoftesting',views.trainingSofttesting,name="trainingsoftesting"),
    path('trainingmanueltesting',views.trainingManuelTesting,name="trainingmanueltesting"),
    path('trainingautotesting',views.trainingAutoTesting,name="trainingautotesting"),
    path('trainingai',views.trainingAI,name="trainingai"),
    path('trainingml',views.trainingML,name="trainingml"),
    path('trainingdata',views.trainingDataScience,name="trainingdata"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
