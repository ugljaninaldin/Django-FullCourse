from django.db import models
from models_guide.models import User

# Create your models here.
class Dean(models.Model):
    int_value = models.IntegerField(null=True, blank=True)
    str_value = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f'Dean number: {self.int_value} is called {self.str_value}.'

class Teacher(models.Model):
    pass

class Diploma(models.Model):
    pass

class Student(models.Model):
    someOtherAppModel = models.ForeignKey(User, on_delete=models.CASCADE)
    dean = models.ForeignKey(Dean, on_delete=models.CASCADE)
    teachers = models.ManyToManyField(Teacher)
    diploma = models.OneToOneField(Diploma, on_delete=models.CASCADE)


# One to Many
# Dean = Dean.objects.create()
#
# Student1 = Student.objects.create(dean=Dean)
# Student2 = Student.objects.create(dean=Dean)

# Many to Many
# Dean = Dean.objects.create()
#
# Teacher1 = Teacher.objects.create()
# Teacher2 = Teacher.objects.create()
#
# Student1 = Student.objects.create(dean=Dean)
# Student2 = Student.objects.create(dean=Dean)
#
# Student1.teachers.add(Teacher1, Teacher2)
# Student2.teachers.add(Teacher2)

# One to One
# Diploma1 = Diploma.objects.create()
# Diploma2 = Diploma.objects.create()
#
# Student1 = Student.objects.create(dean=Dean, diploma=Diploma1)
# Student2 = Student.objects.create(dean=Dean, diploma=Diploma2)