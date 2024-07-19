# # # accounts/models.py

# # from django.contrib.auth.models import AbstractUser
# # from django.db import models

# # class CustomUser(AbstractUser):
# #     # Additional fields
# #     email = models.EmailField(unique=True)
# #     username = models.CharField(max_length=30)
# #     # last_name = models.CharField(max_length=30)

# #     def __str__(self):
# #         return self.username
# from django.db import models
# from django.contrib.auth.models import AbstractUser

# class CustomUser(AbstractUser):
#     # add any custom fields here
#     pass