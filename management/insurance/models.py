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
    def __str__(self):
        return self.User_Id.username +' ' +self.Branch_Code.Name


class Department(models.Model):
    id =models.AutoField(primary_key=True)
    Name=models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
        return self.Name

class Designation(models.Model):
    id =models.AutoField(primary_key=True)
    Name=models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
        return self.Name

class EmployeesinfoM(models.Model):
    id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=255,null=True,blank=True)
    Branch=models.ForeignKey(BranchInformationM,on_delete=models.CASCADE,null=True,blank=True)
    Department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)
    Designation=models.ForeignKey(Designation,on_delete=models.CASCADE,null=True,blank=True)
    Father_Name=models.CharField(max_length=255,null=True,blank=True)
    Mother_Name=models.CharField(max_length=255,null=True,blank=True)
    Married=models.CharField(max_length=255,null=True,blank=True)
    Spouse_Name=models.CharField(max_length=255,null=True,blank=True)
    Sex=models.CharField(max_length=255,null=True,blank=True)
    Birth_Date=models.DateField(null=True,blank=True)
    Present_Address=models.TextField(null=True,blank=True)
    Permanant_Address=models.TextField(null=True,blank=True)
    Phone=models.CharField(max_length=255,null=True,blank=True)
    Email=models.EmailField(null=True,blank=True)
    Nid=models.CharField(max_length=255,null=True,blank=True)
    Joining_Date=models.DateField(null=True,blank=True)
    Probationary_Period=models.CharField(max_length=50,null=True,blank=True)
    Confirmation_dates=models.DateField(null=True,blank=True)
    Status = models.CharField(max_length=100, null=True, blank=True)
    Type = models.CharField(max_length=100, null=True, blank=True)
    Emp_Type = models.CharField(max_length=100, null=True, blank=True)
    objects = models.Manager()

class EmployeesEducation(models.Model):
    id = models.AutoField(primary_key=True)
    Ename=models.ForeignKey(EmployeesinfoM,on_delete=models.CASCADE,null=True,blank=True)
    Exam_Name=models.CharField(max_length=50,null=True,blank=True)
    Institute=models.CharField(max_length=255,null=True,blank=True)
    Board=models.CharField(max_length=50,null=True,blank=True)
    Pass_Year=models.CharField(max_length=50,null=True,blank=True)
    Gpa=models.CharField(max_length=50,null=True,blank=True)
    objects = models.Manager()

class EmployeesSalary(models.Model):
    id = models.AutoField(primary_key=True)
    Ename = models.ForeignKey(EmployeesinfoM, on_delete=models.CASCADE, null=True, blank=True)
    Designation = models.CharField(max_length=255, null=True, blank=True)
    Effect_Date = models.DateField(null=True, blank=True)
    Basic = models.IntegerField(null=True, blank=True)
    House_Rent = models.IntegerField(null=True, blank=True)
    House_Maintenance = models.IntegerField(null=True, blank=True)
    Hospital_Allowance = models.IntegerField(null=True, blank=True)
    Conveyance_Allowance = models.IntegerField(null=True, blank=True)
    Entertainment_Allowance = models.IntegerField(null=True, blank=True)
    Other = models.IntegerField(null=True, blank=True)
    Gross = models.IntegerField(null=True, blank=True)
    Income_Tax = models.IntegerField(null=True, blank=True)
    objects = models.Manager()


class ClientInformation(models.Model):
    id = models.AutoField(primary_key=True)
    Client_Name=models.CharField(max_length=255,null=True,blank=True)
    branch=models.ForeignKey(BranchInformationM,on_delete=models.CASCADE,null=True,blank=True)
    objects = models.Manager()

class ClentAddressInformation(models.Model):
    id = models.AutoField(primary_key=True)
    Client_Name=models.ForeignKey(ClientInformation,on_delete=models.CASCADE,null=True,blank=True)
    Address=models.CharField(max_length=700,null=True,blank=True)
    Phone=models.CharField(max_length=55,null=True,blank=True)
    Email=models.EmailField(max_length=55,null=True,blank=True)
    objects = models.Manager()


class Bankinformation(models.Model):
    id = models.AutoField(primary_key=True)
    Bank_Name=models.CharField(max_length=255,null=True,blank=True)
    branch=models.ForeignKey(BranchInformationM,on_delete=models.CASCADE,null=True,blank=True)
    objects = models.Manager()


class BankBranch(models.Model):
    id = models.AutoField(primary_key=True)
    Bank_Name=models.ForeignKey(Bankinformation,on_delete=models.CASCADE,null=True,blank=True)
    Branch_Name=models.CharField(max_length=700,null=True,blank=True)
    Address=models.CharField(max_length=700,null=True,blank=True)
    Phone=models.CharField(max_length=55,null=True,blank=True)
    Email=models.EmailField(max_length=55,null=True,blank=True)
    objects = models.Manager()

class TransitBy(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=255,null=True,blank=True)
    objects = models.Manager()
    def __str__(self):
        return self.name

class VoyageVia(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=255,null=True,blank=True)
    objects = models.Manager()
    def __str__(self):
        return self.name

class VoyageFrom(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=255,null=True,blank=True)
    objects = models.Manager()
    def __str__(self):
        return self.name

class VoyageTo(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=255,null=True,blank=True)
    objects = models.Manager()
    def __str__(self):
        return self.name


class Currency(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=255,null=True,blank=True)
    objects = models.Manager()
    def __str__(self):
        return self.name


class RiskCover(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=500,null=True,blank=True)
    objects = models.Manager()
    def __str__(self):
        return self.name

class InsuranceType(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=500,null=True,blank=True)
    objects = models.Manager()
    def __str__(self):
        return self.name


class MarineQuatationM(models.Model):
    id = models.AutoField(primary_key=True)
    Bill_date=models.DateField(auto_now=True)
    Insurance_Type=models.ForeignKey(InsuranceType,on_delete=models.CASCADE,null=True,blank=True)
    Client_NameM=models.ForeignKey(ClientInformation,on_delete=models.CASCADE,null=True,blank=True)
    Client_AddressM=models.ForeignKey(ClentAddressInformation,on_delete=models.CASCADE,null=True,blank=True)
    Bank_Name=models.ForeignKey(Bankinformation,on_delete=models.CASCADE,null=True,blank=True)
    Bank_Branch=models.ForeignKey(BankBranch,on_delete=models.CASCADE,null=True,blank=True)
    Bank_Address=models.CharField(max_length=1000,null=True,blank=True)
    Interest_covered=models.CharField(max_length=1000,null=True,blank=True)
    Voyage_From=models.ForeignKey(VoyageFrom,on_delete=models.CASCADE,null=True,blank=True)
    Voyage_To=models.ForeignKey(VoyageTo,on_delete=models.CASCADE,null=True,blank=True)
    Voyage_Via=models.ForeignKey(VoyageVia,on_delete=models.CASCADE,null=True,blank=True)
    Transit_By=models.ForeignKey(TransitBy,on_delete=models.CASCADE,null=True,blank=True)
    Sdate=models.DateField(null=True,blank=True)
    Edate=models.DateField(null=True,blank=True)
    Sum_insured=models.IntegerField(null=True,blank=True)
    Extra1=models.IntegerField(null=True,blank=True)
    Extra2=models.IntegerField(null=True,blank=True)
    Currency=models.IntegerField(null=True,blank=True)
    Excrate=models.IntegerField(null=True,blank=True)
    Bdtamount=models.IntegerField(null=True,blank=True)
    Declaration=models.CharField(max_length=600,null=True,blank=True)
    Producer=models.CharField(max_length=600,null=True,blank=True)
    RiskCover=models.ForeignKey(RiskCover,on_delete=models.CASCADE,null=True,blank=True)












