from django.db import models

# Recursive realations, related names
class Person(models.Model):
    mother = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name="son")
    siblings = models.ManyToManyField('self', blank=True)
    partner = models.OneToOneField('self', on_delete=models.CASCADE, null=True, blank=True, related_name="ppartner")

# How to use this realtions in py
# Creates empty object that represent mother object
# Mary = Person.objects.create()
# Mary.save()
# Create person object 
# Jhon = Person.objects.create(mother=Mary)
# Jhon.mother --> prints out object that lead to Jhon's mother
# Mary.son.get() --> uses "related_name" to return Mary's son (Jhon's object)