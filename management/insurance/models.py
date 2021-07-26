from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BranchInformationM(models.Model):
    id=models.AutoField(primary_key=True)
    Company_Name=models.CharField(max_length=255,null=True,blank=True)
    Name=models.CharField(max_length=255,null=True,blank=True)
    Address=models.TextField(max_length=500,null=True,blank=True)
    Short_Name=models.CharField(max_length=50,null=True,blank=True)
    Phone=models.CharField(max_length=50,null=True,blank=True)
    Fax=models.CharField(max_length=50,null=True,blank=True)
    Email=models.EmailField(max_length=50,null=True,blank=True)
    Branch_Code=models.CharField(max_length=100,null=True,blank=True)
    BranchLogo=models.ImageField(upload_to='logo',null=True,blank=True)
    objects=models.Manager()

    def logo(self):
        try:
            urls = self.BranchLogo.url
        except:
            urls = ''
        return urls


class UserProfileM(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    Phone=models.CharField(max_length=100,null=True,blank=True)
    Present_Address=models.TextField(max_length=255,null=True,blank=True)
    Permanant_Address=models.TextField(max_length=255,null=True,blank=True)
    Image=models.ImageField(upload_to='User_image',null=True,blank=True)
    objects=models.Manager()

    def uimages(self):
        try:
            urls=self.Image.url
        except:
            urls=''
        return urls

class UserBranchM(models.Model):
    id = models.AutoField(primary_key=True)
    User_Id=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    Branch_Code=models.ForeignKey(BranchInformationM,on_delete=models.CASCADE,null=True,blank=True)
    objects=models.Manager()

