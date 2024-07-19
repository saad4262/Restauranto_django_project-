# models.py
from django.db import models

class ChefModels(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chef_images', null=True, blank=True)

    def __str__(self):
        return self.name




from django.db import models

class AdminProfile(models.Model):
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

