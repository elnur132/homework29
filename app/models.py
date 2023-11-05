from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    teacher = models.ManyToManyField(Teacher, related_name='students')

    def __str__(self):
        return self.name
