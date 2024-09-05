from django.db import models

# Create your models here.
class Books(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=220)
    publication=models.DateField()
    def __str__(self) :
        return self.name