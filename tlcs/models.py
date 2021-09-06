from django.db import models

# Create your models here.
class Contacts(models.Model):
    sno=models.AutoField(primary_key=True)
    firstName=models.CharField(max_length=255)
    lastName=models.CharField(max_length=255)
    business_field=models.CharField(max_length=200)
    phone=models.IntegerField()
    email=models.EmailField(max_length=150)
    message=models.TextField()
