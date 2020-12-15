from django.db import models


class Gallerie(models.Model):
    titre = models.CharField(max_length=250)
    image = models.ImageField(upload_to='gallerie/images/')
    date = models.DateField()
