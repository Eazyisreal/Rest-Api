from ctypes import addressof
from statistics import mode
from django.db import models
from pkg_resources import working_set

# Create your models here.
class Contact(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country =  models.CharField(max_length=100)
    home_phone = models.IntegerField(null=True, blank=True)
    work_phone = models.IntegerField(null=True, blank=True)
    home_other = models.IntegerField(null=True, blank=True)
    mobile_primary = models.IntegerField(null=True, blank=True)
    mobile_secondary = models.IntegerField(null=True, blank=True)
    