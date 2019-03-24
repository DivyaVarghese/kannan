import datetime
from django.utils import timezone
from jsonfield import JSONField
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CustomerR(models.Model):
	cid=models.AutoField(primary_key=True)
	user1=models.ForeignKey(User,on_delete=models.CASCADE)
	name1=models.CharField(max_length=15)
	location=models.CharField(max_length=20)
	pho=models.CharField(max_length=15)
	category=models.CharField(max_length=2,default=1)
	def __str___(self):
		return self.name1

class HotelReg(models.Model):
	hid=models.AutoField(primary_key=True)
	user1=models.ForeignKey(User,on_delete=models.CASCADE)
	location=models.CharField(max_length=20)
	ftype=models.CharField(max_length=20)
	permitno=models.CharField(max_length=10)
	opent=models.CharField(max_length=5)
	closet=models.CharField(max_length=5)
	pho=models.CharField(max_length=15)
	name1=models.CharField(max_length=15)
	address=models.TextField()
	category=models.CharField(max_length=2,default=2)
	image=models.FileField(upload_to='media',blank=True)
	rating=models.CharField(max_length=10)

	def  __str__(self):
		return self.name1

class Foodlist(models.Model):
	fid=models.AutoField(primary_key=True)
	hotel=models.ForeignKey(HotelReg,on_delete=models.CASCADE)
	foodid=models.CharField(max_length=5)
	hid=models.CharField(max_length=3)
	foodname=models.CharField(max_length=20)
	prize=models.CharField(max_length=5)
	chef=models.CharField(max_length=20)
	details=models.TextField()
	time=models.CharField(max_length=5)
	img=models.FileField(upload_to='media',blank=True)
	atime=models.CharField(max_length=10)
	def __str__(self):
		return self.foodname

class Cart(models.Model):
	orderid=models.AutoField(primary_key=True)
	cid=models.ForeignKey(CustomerR,on_delete=models.CASCADE)
	hid=models.ForeignKey(HotelReg,on_delete=models.CASCADE)
	customerid=models.CharField(max_length=10)
	hotelid=models.CharField(max_length=10)
	order=JSONField(blank=True,null=True)
	totamt=models.CharField(max_length=5)
	payment=models.CharField(max_length=5)
	status=models.CharField(max_length=2,default=0)
	date=models.DateTimeField(default=datetime.datetime.now(), blank=True)
	def __str__(self):
		return self.cid.name1
class Order(models.Model):
	orderid=models.CharField(max_length=5)
	location=models.TextField()
	pho=models.CharField(max_length=10)
	payment=models.CharField(max_length=20)
	def __str__(self):
		return self.orderid
class Offer(models.Model):
	cutoff=models.CharField(max_length=8)
	offerper=models.CharField(max_length=5)
	date=models.DateTimeField(default=datetime.datetime.now(),blank=True)
	def __str__(self):
		return self.offerper
class Rate(models.Model):
	orderid=models.ForeignKey(Order,on_delete=models.CASCADE)
	hid=models.ForeignKey(HotelReg,on_delete=models.CASCADE)
	hotelid=models.CharField(max_length=10)
	cid=models.ForeignKey(CustomerR,on_delete=models.CASCADE)
	customerid=models.CharField(max_length=10)
	rating=models.CharField(max_length=20)
	time=models.CharField(max_length=10)
	date=models.DateTimeField(default=datetime.datetime.now(),blank=True)
	def __str__(self):
		return self.hotelid
