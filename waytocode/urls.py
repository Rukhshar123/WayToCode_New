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
from tutorials import views as tutorial
from adminside import views as adminside
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
    path('asp.net',web.aspnetTechnology,name="asp.net"),
    path('python',web.pythonTechnology,name="python"),
    path('java',web.javaTechnology,name="java"),
    path('php',web.phpTechnology,name="php"),
    path('android',web.androidTechnology,name="android"),
    path('ios',web.iosTechnology,name="ios"),
    path('angularjs',web.angularjsTechnology,name="angularjs"),
    path('nodejs',web.nodejsTechnology,name="nodejs"),
    path('reactjs',web.reactjsTechnology,name="reactjs"),
    path('ror',web.rorTechnology,name="ror"),
    path('golang',web.golangTechnology,name="golang"),

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
    path('blogs',training.blogs,name="blogs"),

    #Admin URLs
    path('adminregister',adminside.adminRegister,name="adminregister"),
    path('adminlogin',adminside.adminLogin,name="adminlogin"),
    path('adminhome',adminside.adminHome,name="adminhome"),
    path('logout',adminside.logout,name="logout"),
    path('getemail',adminside.getEmail,name="getemail"),
    path('forgotpassword',adminside.forgotPassword,name="forgotpassword"),
    path('editprofile/<int:id>',adminside.editProfile,name="editprofile"),
    path('addservices',adminside.addServices,name="addservices"),
    path('allservices',adminside.allServices,name="allservices"),
    path('editServices/<int:id>',adminside.editServices,name="editervices"),
    path('updateServices/<int:id>',adminside.updateServices,name="updateservices"),
    path('deleteServices/<int:id>',adminside.deleteServices,name="deleteservices"),
    path('addpossibility',adminside.addPossibility,name="addpossibilty"),
    path('allpossibility',adminside.allPossibility,name="allpossibility"),
    path('editpossibility/<int:id>',adminside.editPossibility,name="editpossibility"),
    path('updatepossibility/<int:id>',adminside.updatePossibility,name="updatepossibility"),
    path('deletepossibility/<int:id>',adminside.deletePossibility,name="deletepossibilty"),
    path('addreview',adminside.addReview,name="addreview"),
    path('allreview',adminside.allReview,name="allreview"),
    path('editreview/<int:id>',adminside.editReview,name="editreview"),
    path('updatereview/<int:id>',adminside.updateReview,name="updatereview"),
    path('deletereview/<int:id>',adminside.deleteReview,name="deletereview"),
    path('addteam',adminside.addTeam,name="addteam"),
    path('allteam',adminside.allTeam,name="allteam"),
    path('editteam/<int:id>',adminside.editTeam,name="editteam"),
    path('updateteam/<int:id>',adminside.updateTeam,name="updateteam"),
    path('deleteteam/<int:id>',adminside.deleteTeam,name="deleteteam"),
    path('addportfolio',adminside.addPortfolio,name="addportfolio"),
    path('allportfolio',adminside.allPortfolio,name="allportfolio"),
    path('editportfolio/<int:id>',adminside.editPortfolio,name="editportfolio"),
    path('updateportfolio/<int:id>',adminside.updatePortfolio,name="updateportfolio"),
    path('deleteportfolio/<int:id>',adminside.deletePortfolio,name="deleteportfolio"),
    path('addtechnology',adminside.addTechnology,name="addtechnology"),
    path('alltechnology',adminside.allTechnology,name="alltechnology"),
    path('edittechnology/<int:id>',adminside.editTechnology,name="edittechnology"),
    path('updatetechnology/<int:id>',adminside.updateTechnology,name="updatetechnology"),
    path('deletetechnology/<int:id>',adminside.deleteTechnology,name="deletetechnology"),
    path('addcareer',adminside.addCareer,name="addcareer"),
    path('allcareer',adminside.allCareer,name="allcareer"),
    path('editcareer/<int:id>',adminside.editCareer,name="editcareer"),
    path('updatecareer/<int:id>',adminside.updateCareer,name="updatecareer"),
    path('deletecareer/<int:id>',adminside.deleteCareer,name="deletecareer"),
    path('addtraining',adminside.addTraining,name="addtraining"),
    path('alltraining',adminside.allTraining,name="alltraining"),
    path('edittraining/<int:id>',adminside.editTraining,name="edittraining"),
    path('updatetraining/<int:id>',adminside.updateTraining,name="updatetraining"),
    path('deletetraining/<int:id>',adminside.deleteTraining,name="deletetraining"),
    path('addstudentreview',adminside.addStudentreview,name="addstudentreview"),
    path('allstudentreview',adminside.allStudentreview,name="allstudentreview"),
    path('editstudentreview/<int:id>',adminside.editStudentreview,name="editstudentreview"),
    path('updatestudentreview/<int:id>',adminside.updateStudentreview,name="updatestudentreview"),
    path('deletestudentreview/<int:id>',adminside.deleteStudentreview,name="deletestudentreview"),
    path('addcourse',adminside.addCourse,name="addcourse"),
    path('allcourse',adminside.allCourse,name="allcourse"),
    path('editcourse/<int:id>',adminside.editCourse,name="editcourse"),
    path('updatecourse/<int:id>',adminside.updateCourse,name="updatecourse"),
    path('deletecourse/<int:id>',adminside.deleteCourse,name="deletecourse"),
    path('addblog',adminside.addBlog,name="addblog"),
    path('allblog',adminside.allBlog,name="allblog"),
    path('editblog/<int:id>',adminside.editBlog,name="editblog"),
    path('updateblog/<int:id>',adminside.updateBlog,name="updateblog"),
    path('deleteblog/<int:id>',adminside.deleteBlog,name="deleteblog"),
    #Tutorial URLs
    path('C_home',tutorial.CHome,name="C_home"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
