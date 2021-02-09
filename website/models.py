from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    description_first = models.TextField()
    description_second = models.TextField()
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
    image = models.ImageField(upload_to='images/portfolio')

class Technology(models.Model):
    name = models.CharField(max_length=100)
    description_first = models.TextField()
    description_second = models.TextField()
    benefits = models.TextField()

class Career(models.Model):
    position_name = models.CharField(max_length=100)
    about = models.TextField()
    job_requirements = models.TextField()
    job_responsibilities = models.TextField()
    benefits = models.TextField()





