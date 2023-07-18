from django.db import models
from admins.models import Products

# Create your models here.
class Register(models.Model):
    cname = models.CharField(max_length=50)
    cemail = models.CharField(max_length=50)
    paw = models.CharField(max_length=50)
    mno= models.CharField(max_length=50)
    addr = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)


class Purchase(models.Model):
    pname= models.CharField(max_length=50)
    pcat=models.CharField(max_length=50)
    pcost = models.CharField(max_length=50)
    pquality= models.CharField(max_length=50)
    pdec= models.CharField(max_length=50)
    cid= models.ForeignKey(Register,on_delete=models.DO_NOTHING)
    pid=models.ForeignKey(Products,on_delete=models.DO_NOTHING)

