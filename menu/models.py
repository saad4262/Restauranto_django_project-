from django.db import models

class MenuModel(models.Model):
    image = models.ImageField(null=True,blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.title
