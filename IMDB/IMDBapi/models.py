from django.db import models

# Create your models here.
class IMDBdata(models.Model):
    Title = models.CharField(max_length=50)
    Year = models.IntegerField()
    Rating = models.FloatField()
    ImgUrl = models.CharField(max_length=250)
    