from django.db import models
from datetime import datetime

# Create your models here.
class principalModel(models.Model):
    name=models.CharField(max_length=70)
    qualification=models.TextField()
    city=models.CharField(max_length=100)
    appionted_on=models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name