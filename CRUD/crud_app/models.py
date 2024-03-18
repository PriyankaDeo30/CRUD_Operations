from django.db import models

# Create your models here.
class UserModel(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=15)

    def __str__(self):
        return self.first_name

