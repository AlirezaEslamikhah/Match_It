from django.db import models

class person(models.Model):
    username = models.CharField( null = True ,blank= True,max_length=250)
    #password = models.CharField( null= True , blank= True,max_length=255)
    type = models.CharField(null=True,blank=True,max_length=250)
    city = models.CharField(null=True,blank=True,max_length=3)
    #email = models.EmailField(null=True,blank=True,max_length=255) 
    type_cmplement = models.CharField(null=True,blank=True,max_length=250)
    sen = models.CharField(null=True,blank=True,max_length=250)