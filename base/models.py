from django.contrib.auth.models import User
from django.db import models

class From_Station(models.Model):
    name = models.CharField(max_length=50,primary_key=True)
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.name

class To_Station(models.Model):
    name = models.CharField(max_length=50,primary_key=True)
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.name        

class Train(models.Model):
    name = models.CharField(max_length=50,primary_key=True)
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.name      


class Train_Route(models.Model):
    name = models.CharField(max_length=50,primary_key=True)
    code = models.CharField(max_length=7)
    train = models.ForeignKey(Train,on_delete=models.CASCADE)
    From = models.ForeignKey(From_Station,on_delete=models.CASCADE)
    To = models.ForeignKey(To_Station,on_delete=models.CASCADE)
    price = models.IntegerField(null=True)
    duration = models.IntegerField(null=True)
    time = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.name  


class Booking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    route = models.ForeignKey(Train_Route,on_delete=models.CASCADE)
    useraddress = models.CharField(max_length=100)
    userphonenumber = models.IntegerField()
    pnr_number = models.CharField(max_length=20,null=True,blank=True)

    def __str__(self):
        return f"{self.pnr_number}  {self.user}  {self.route}" 
