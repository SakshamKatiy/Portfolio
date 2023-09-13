from django.db import models

# Create your models here.
class message(models.Model):
    name= models.CharField( max_length=50)
    email= models.EmailField( max_length=50)
    msg= models.CharField( max_length=50)