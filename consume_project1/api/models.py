from django.db import models

# Create your models here.
class Student(models.Model):
    name =models.CharField(max_length = 50)
    rollno = models.IntegerField()
    city = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length = 50)
    rollno = models.IntegerField()
    city = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
