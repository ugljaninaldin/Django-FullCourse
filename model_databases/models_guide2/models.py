from django.db import models

# Create your models here.
class Dean(models.Model):
    pass

class Teacher(models.Model):
    pass

class Diploma(models.Model):
    pass

class Student(models.Model):
    dean = models.ForeignKey(Dean, on_delete=models.CASCADE)
    teachers = models.ManyToManyField(Teacher)


# One to Many
# Dean = Dean.objects.create()
#
# Student1 = Student.objects.create(dean=Dean)
# Student2 = Student.objects.create(dean=Dean)

# Many to Many
# Dean = Dean.objects.create()
#
# Teacher1 = Teacher.objects.create(dean=Dean)
# Teacher2 = Teacher.objects.create(dean=Dean)
#
# Student1 = Student.objects.create(dean=Dean)
# Student2 = Student.objects.create(dean=Dean)
#
# Student1.teachers.add(Teacher1, Teacher2)
# Student2.teachers.add(Teacher2)

# One to One