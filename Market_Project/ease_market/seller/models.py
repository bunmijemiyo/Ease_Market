from django.db import models

# Create your models here.


class Seller(models.Model):
    name = models.CharField(max_length=64)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    # image = models.FilePathField()
    #image = models.ImageField(upload_to ='uploads/')





