from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator,MaxLengthValidator,RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError
Create your models here.
class User(AbstractUser):
    pass 

class Doctor(User):

    license_number =models.CharField(max_length=100,unique=True,validators=[MinLengthValidator(6),MaxLengthValidator(6)])
    #obligatoirement max_length pour la creation du base de donnée sinon il provoque un erreur
    phone = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    specialities = models.ManyToManyField("AccountApp.Specialty", related_name="doctors")

number_validator = RegexValidator(
            regex=r'^\d{8}$',
            message='This number must contain 8 digits'
        )

def validate_birth_date(v):
    if v > timezone.localdate():
        rais