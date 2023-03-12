from django.db import models
from listings.models import Listing
from django.contrib.auth.models import User
# Create your models here.

class Bookings(models.Model):
    listing_id = models.ForeignKey(Listing ,null=True,on_delete=models.CASCADE)
    #listing_id = models.IntegerField(null=True)
    name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100,blank=True)
    phone_number = models.BigIntegerField(max_length=100,blank=True)
    adhar_card = models.CharField(max_length=100,blank=True)
    pan_card = models.CharField(max_length=100,blank=True)
    family_members = models.CharField(max_length=100,blank=True)
    aggrement = models.FileField(upload_to='aggrement/%Y/%m/%d')
    user_id = models.ForeignKey( User, null=True,on_delete= models.CASCADE)
    #user_id = models.IntegerField( null=True)

    def __str__(self):
        return self.name