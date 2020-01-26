from django.db import models

# Create your models here.

class Imagemodels(models.Model):
    name= models.CharField(max_length=122,blank=False)
    image=models.ImageField()

    def __str__(self):
        return str(self.name)