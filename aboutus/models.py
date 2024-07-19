from django.db import models

class AboutUs(models.Model):
    image = models.ImageField(null=True,blank=True)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    description = models.TextField()
    # read_more_link = models.URLField(blank=True)  # Field for storing URLs
    
    # read_more_link = models.URLField(blank=True)

    def __str__(self):
        return self.title
    

from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to='profiles/')

    def __str__(self):
        return self.name
