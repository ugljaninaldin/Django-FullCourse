from django.contrib import admin
from .models import Dean, Teacher, Student, Diploma

# Register your models here.
admin.site.register((Dean, Teacher, Student, Diploma))