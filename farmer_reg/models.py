from django.db import models
from userauths.models import CustomUser as User

# Create your models here.
class Farmer(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=20, blank=False, null=False)
    surname = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11,unique=True, blank=False, null=False)

    lga = models.CharField(max_length=20, blank=True, null=True)
    farm_name = models.CharField(max_length=20, blank=True)

    reg_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.User.username

