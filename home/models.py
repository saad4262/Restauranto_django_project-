
from django.db import models


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)  
    email = models.EmailField(max_length=100)
    num_people = models.IntegerField()
    date = models.DateField()
    message = models.TextField(blank=True)



    def __str__(self):
        return self.name





class Email(models.Model):
    recipient = models.EmailField()
    

