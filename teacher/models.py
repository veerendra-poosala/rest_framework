from django.db import models

# Create your models here.

class teacherModel(models.Model):
    name=models.CharField(max_length=70)
    salary=models.IntegerField()
    subject=models.CharField(max_length=100)
    feedback=models.TextField()

    def __str__(self):
        return self.name