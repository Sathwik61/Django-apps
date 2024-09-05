from django.db import models

# Create your models here.
class Project(models.Model):
    topic=models.CharField(max_length=120)
    duration=models.CharField(max_length=200)
    languages=models.TextField(max_length=300)
    def __str__(self):
        return self.topic
    
class Students(models.Model):
    name=models.CharField(max_length=120)
    email=models.EmailField()
    project=models.ManyToManyField(Project,related_name='projectname')
    def __str__(self):
        return self.name

