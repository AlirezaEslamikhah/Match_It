from django.db import models

class person(models.Model):
    username = models.CharField( null = True ,blank= True,max_length=250)
    password = models.CharField( null= True , blank= True,max_length=255)
    name = models.CharField(null=True,blank=True,max_length=250)
    age = models.CharField(null=True,blank=True,max_length=3)
    email = models.EmailField(null=True,blank=True,max_length=255) 