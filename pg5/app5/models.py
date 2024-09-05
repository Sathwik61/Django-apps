from django.db import models

# Create your models here.
class Cources(models.Model):
    name=models.CharField(max_length=150)
    description=models.TextField(max_length=250)
    def __str__(self) :
        return self.name
class Students(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField()
    cources=models.ManyToManyField(Cources,related_name="students")
    def __str__(self) :
        return self.name
