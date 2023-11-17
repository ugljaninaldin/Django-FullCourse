from typing import Any
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
def int_is_evean(value):
    if (value % 2 != 0):
        raise ValidationError(str(value) + " is not even.")

class EvenInteger(models.IntegerField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators.append(int_is_evean)

class MyModel(models.Model):
    # even_int = models.IntegerField(validators=[int_is_evean])
    even_int = EvenInteger()
