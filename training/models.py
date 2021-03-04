from django.db import models

class Training(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/training')
    link = models.CharField(max_length=100, default=None)

class StudentReview(models.Model):
    name = models.CharField(max_length=100)
    designation = models.TextField()
    review = models.TextField()
    image = models.ImageField(upload_to='images/studentreview')

class TrainingTechnology(models.Model):
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/course')


class Blog(models.Model):
    technology = models.CharField(max_length=100, default=None)
    header = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/blog')
    date = models.DateField(max_length=12)
    name = models.CharField(max_length=100, default=None)


class TrainingContact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    message = models.TextField()



