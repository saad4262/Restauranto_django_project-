from django.db import models

class dealsModel(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='chefimages/', blank=True,null=True)

    def __str__(self):
        return self.name
