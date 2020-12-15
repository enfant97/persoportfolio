from django.db import models


class Project(models.Model):
    titre = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='project/images/')
