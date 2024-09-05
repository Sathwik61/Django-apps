from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=700)
    email=models.EmailField()
    phone=models.CharField(max_length=300)
    def __str__(self):
        return self.name