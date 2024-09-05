from django.db import models

# Create your models here.
class Courses(models.Model):
    name=models.CharField(max_length=120)
    def __str__(self) :
        return self.name

class Students(models.Model):
    name=models.CharField(max_length=120)
    email=models.EmailField()
    courses=models.ManyToManyField(Courses,related_name="cources")
    def __str__(self) :
        return self.name
