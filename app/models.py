from django.db import models

# Create your models here.

class Carousel(models.Model):
    image = models.ImageField(upload_to='images/',)
    title = models.CharField(max_length=250,)
    description = models.CharField(max_length=250,)


    def __str__(self):
        return self.title
