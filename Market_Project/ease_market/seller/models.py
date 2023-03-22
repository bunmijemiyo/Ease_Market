from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Seller(models.Model):
    name = models.CharField(max_length=64)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    slug = models.SlugField()
    thumb = models.ImageField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    # image = models.FilePathField()
    #image = models.ImageField(upload_to ='uploads/')


    def __str__(self):
        return self.name


