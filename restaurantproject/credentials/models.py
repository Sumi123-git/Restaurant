from django.db import models

# Create your models here.
class reserve(models.Model):
    name=models.CharField(max_length=120)
    email=models.EmailField()
    vegetarian=models.TextField(max_length=110)
    non_vegetarian=models.TextField(max_length=110)
    phonenumber=models.IntegerField()

    def __str__(self):
        return self.name
