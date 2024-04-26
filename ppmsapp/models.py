from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from pydoc import describe

# Create your models here.
class Category(models.Model):       #admin....
    product_category = models.CharField(max_length=100)
    product_price = models.IntegerField()
    product_stock = models.IntegerField()
    
class Report(models.Model):       #user....
    r_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    r_category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    r_name=models.CharField(max_length=60)
    r_DOB = models.DateField()
    r_details=models.CharField(max_length=500)
    r_quantity = models.IntegerField(null=True)
    
class Employee(models.Model):       #user....
    e_category =models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    e_report = models.ForeignKey(Report, on_delete=models.CASCADE,null=True)
    e_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    e_fname = models.CharField(max_length=30)
    e_lname = models.CharField(max_length=30)
    e_address = models.CharField(max_length=100)
    e_age=models.IntegerField()
    e_phone_numbr = models.BigIntegerField(10)
    e_email = models.EmailField()
    e_post=models.CharField(max_length=20)
    e_photo = models.ImageField(upload_to='image/',null=True)
    e_shift=models.CharField(max_length=30)
    
class Attendance(models.Model):
    a_user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    a_attendnce=models.CharField(max_length=30)
    a_DOB = models.DateField()
    a_post=models.CharField(max_length=30)

class Leave(models.Model):
    l_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    l_req=models.CharField(max_length=50)
    l_reason=models.CharField(max_length=100)
    
class Petrol(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    status = models.CharField(max_length=2,choices=(('1','Active'),('0', 'Inactive')) , default = 1)
    price = models.FloatField(max_length=(15,2), default= 0)
    delete_flag = models.IntegerField(default = 0)
    date_added = models.DateTimeField(default = timezone.now)
    date_created = models.DateTimeField(auto_now = True)

class Stock(models.Model):
    date = models.DateField(null=True, blank = True)
    petrol = models.ForeignKey(Petrol, on_delete=models.CASCADE)
    volume = models.FloatField(max_length=(15,2), default=0)
    date_added = models.DateTimeField(default = timezone.now)
    date_created = models.DateTimeField(auto_now = True)


class Sale(models.Model):
    date = models.DateField(null=True, blank = True)
    customer_name = models.CharField(max_length=250)
    petrol = models.ForeignKey(Petrol, on_delete=models.CASCADE)
    volume = models.FloatField(max_length=(15,2), default=0)
    price = models.FloatField(max_length=(15,2), default=0)
    amount = models.FloatField(max_length=(15,2), default=0)
    date_added = models.DateTimeField(default = timezone.now)
    date_created = models.DateTimeField(auto_now = True)





    

