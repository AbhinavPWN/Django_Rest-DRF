from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    qualification = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    