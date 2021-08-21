from django.db import models

# Create your models here.
class secuirity_staffModel(models.Model):
    name=models.CharField(max_length=70)
    salary=models.IntegerField()
    city=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
