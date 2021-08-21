from django.db import models
from django.db.models.fields import CharField

# creating student model 

class studentModel(models.Model):
    name=models.CharField(max_length=70)
    roll_no=models.IntegerField()
    fee=models.IntegerField()
    grade=models.CharField(max_length=30)

    def __str__(self):
        return self.name


