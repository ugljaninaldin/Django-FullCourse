from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=40, verbose_name="Ime")
    last_name = models.CharField(max_length=40, verbose_name="Prezime")
    email = models.EmailField(max_length=255, default="", verbose_name="Mail", unique=True)
    GENDER_CHOISES = {
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    }
    gender = models.CharField(max_length=1, choices=GENDER_CHOISES, default="M", verbose_name="Pol")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Table for User
# models_guide_user:
#     id
#     first_name
#     last_name
#     gender(GENDER_CHOISES)