from django.db import models

class Training(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/training')

class StudentReview(models.Model):
    name = models.CharField(max_length=100)
    designation = models.TextField()
    review = models.TextField()
    image = models.ImageField(upload_to='images/studentreview')

class Course(models.Model):
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/course')


class Blog(models.Model):
    header = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/blog')
    date = models.DateField(max_length=12)



