from django.db import models

class ChefsModel(models.Model):
    image = models.ImageField(null=True,blank=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    # description = models.TextField()
    # read_more_link = models.URLField(blank=True)

    # def __str__(self):
    #     return self.title