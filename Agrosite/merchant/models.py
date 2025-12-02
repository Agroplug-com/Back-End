from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Buyer(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=20, blank=False, null=False)
    surname = models.CharField(max_length=20, blank=False, null=False)
    phone = models.CharField(max_length=11, blank=False, null=False, unique=True)
    email = models.EmailField(unique=True)
    lga = models.CharField(max_length=20, blank=False)
    location = models.TextField(max_length=100, blank=False, null=False)

    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name
