from django.db import models

class Applicant(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    # JOB_TYPE_CHOICES = [
    #     ('part-time', 'Part-Time'),
    #     ('full-time', 'Full-Time'),
    # ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    job_type = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.name



