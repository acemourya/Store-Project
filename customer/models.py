from django.db import models
from django.core.validators import RegexValidator


class User(models.Model):
    """ Create user model fields """

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number_regex = RegexValidator(regex=r"^\+?91?\d{8,15}$")
    phone_number = models.CharField(
        validators=[phone_number_regex], max_length=15, unique=True, null=False)


class Customer(models.Model):
    """ Create customer model fields with one to one releationship """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_number = models.IntegerField(unique=True, null=False, default=0)

    def __int__(self):
        return self.profile_number
