from django.db import models

# Create your models here.
class Person(models.Model):
    birth_year = models.IntegerField()

    def __str__(self):
        return f'{self.birth_year}'