from django.db import models
from django.contrib.auth.models import User
import datetime
import os

# Create your models here.
def getfilename(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_file="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_file)

class Catagory(models.Model):
    new_cat=models.CharField(max_length=30,null=False,blank=False)

    def __str__(self):
        return self.new_cat
 

class post(models.Model):
    catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,null=False,blank=False)
    body=models.CharField(max_length=500,null=False,blank=False)
    author=models.CharField(max_length=50,null=False,blank=False)
    images=models.ImageField(upload_to=getfilename,null=False,blank=False)
    type=models.CharField(max_length=30,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        
class createpost(models.Model):
    catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,null=False,blank=False)
    body=models.CharField(max_length=500,null=False,blank=False)
    author=models.CharField(max_length=50,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    images=models.ImageField(upload_to=getfilename,null=False,blank=False)
    type=models.CharField(max_length=30,null=False,blank=False)

    def __str__(self):
        return self.title

class User_details(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    About=models.TextField(max_length=50,null=False,blank=False)
    image=models.FileField(upload_to=getfilename)

    