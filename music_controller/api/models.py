from django.db import models
import string
import random

# Create your models here.
# Django allows us to perform data base operations using python





def geneate_unique_code():
    length =6 

    while True:
        code="".join(random.choices(string.ascii_uppercase,k=length))# creating a unique random 8 characters asci code
        if Room.objects.filter(code=code).count==0:
            break  #Room.objects.filter returns a list of all room object that has their code attribute == to the random code created on top
                    #if the if statements does not find an ranodm code on the first itteration, it will continue to loop given the while TRUE
    return code #return the unique CODE



class Room(models.Model):
    code = models.CharField((""), max_length=8,unique=True)#This would represent the ROOM  8 digits id, which is why it is unique. Max length is 8, and the default value is ""
    host= models.CharField(max_length=8,unique=True) # This would represent the current host, and he has a unique ID of 8 digits
    guest_can_pause=models.BooleanField(null=False,default=False) # boolean value to know if user can pause the music. 
    votes_to_skip=models.IntegerField(null=False,default=1) #field that keeps track of how many votes to skip are they 
    created_at=models.DateTimeField(auto_now_add=True) # Time for creation request. 





#dont forget to make migrations when we modify the database