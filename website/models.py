from django.db import models
from ckeditor.fields import RichTextField

class Service(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    description_first = models.TextField()
    description_second = models.TextField()
    link =  models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/services')

class MaximumPossibilities(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/MaximumPossibility')

class Reviews(models.Model):
    name = models.CharField(max_length=100)
    reviews = models.TextField()
    image = models.ImageField(upload_to='images/reviews')

class Team(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/team')


class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='images/portfolio')
    image2 = models.ImageField(upload_to='images/portfolio',default='web4.jpg')

class Technology(models.Model):
    name = models.CharField(max_length=100)
    description_first = models.TextField()
    description_second = models.TextField()
    image1 = models.ImageField(upload_to='images/technology',default=None)
    image2 = models.ImageField(upload_to='images/technology',default=None)

class Career(models.Model):
    position_name = models.CharField(max_length=100)
    about = models.TextField()
    job_requirements = RichTextField(blank=True, null=True)
    job_responsibilities = RichTextField(blank=True, null=True)
    benefits = RichTextField(blank=True, null=True)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField(max_length=12)
    description = models.TextField()





