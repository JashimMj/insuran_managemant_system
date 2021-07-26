from django.shortcuts import render,redirect
from django.contrib import auth,messages
from django.core.files.storage import FileSystemStorage
from .models import *
from django.http import HttpResponseRedirect
# Create your views here.

def indexV(request):
    company = BranchInformationM.objects.filter(Branch_Code=1)
    userprofile = UserProfileM.objects.filter(id=request.user.id)
    return render(request,'index.html',{'company':company,'userprofile':userprofile})

def mainV(request):
    company = BranchInformationM.objects.filter(Branch_Code=1)
    ubranch= UserBranchM.objects.filter(User_Id=request.user.id)
    userprofile=UserProfileM.objects.filter(user=request.user.id)
    currentbranch=BranchInformationM.objects.raw('select a.id,a.Name from insurance_branchinformationm a,auth_user b where b.id=%s and a.branch_code=b.last_name',[request.user.id])
    return render(request,'pages/main.html',{'company':company,'userprofile':userprofile,'ubranch':ubranch,'currentbranch':currentbranch})


def maindashboardV(request):
    company = BranchInformationM.objects.filter(Branch_Code=1)
    return render(request,'pages/maindashboard.html',{'company':company})


def admindashboardV(request):
    company = BranchInformationM.objects.filter(Branch_Code=1)
    return render(request,'admin/admindashboard.html',{'company':company})


def branchinfoV(request):
    company = BranchInformationM.objects.filter(Branch_Code=1)
    companys = BranchInformationM.objects.all()
    return render(request,'admin/forms/branchinfo.html',{'company':company,'companys':companys})

def branchinfosaveV(request):
    if request.method =='POST' and request.FILES:
        cname=request.POST.get('cname')
        names=request.POST.get('name')
        addresss=request.POST.get('address')
        snames=request.POST.get('sname')
        phones=request.POST.get('phone')
        faxs=request.POST.get('fax')
        emails=request.POST.get('email')
        bcodes=request.POST.get('bcode')
        image = request.FILES['logo']
        store = FileSystemStorage()
        filename = store.save(image.name, image)
        profile_pic_url = store.url(filename)
        data =BranchInformationM (Name=names, Address=addresss, Short_Name=snames,Phone=phones,Fax=faxs,
                                  Email=emails,Branch_Code=bcodes,BranchLogo=filename,Company_Name=cname)
        data.save()
        messages.info(request, 'Data Saved')
    else:
        cname = request.POST.get('cname')
        names = request.POST.get('name')
        addresss = request.POST.get('address')
        snames = request.POST.get('sname')
        phones = request.POST.get('phone')
        faxs = request.POST.get('fax')
        emails = request.POST.get('email')
        bcodes = request.POST.get('bcode')
        data = BranchInformationM(Name=names, Address=addresss, Short_Name=snames, Phone=phones, Fax=faxs,
                                  Email=emails, Branch_Code=bcodes, Company_Name=cname)
        data.save()
        messages.info(request, 'Data Saved')

    return redirect('/branch/information/')


def branchinfoeditV(request,id=0):
    company = BranchInformationM.objects.filter(Branch_Code=1)
    companys = BranchInformationM.objects.all()
    if id != 0:
        companyedit = BranchInformationM.objects.filter(pk=id)
    return render(request,'admin/forms/branchinfoedit.html',{'company':company,'companyedit':companyedit,'companys':companys})


def branchinfoupdateV(request,id=0):
    ima = BranchInformationM.objects.get(pk=id)
    if id !=0:
        cname = request.POST.get('cname')
        names = request.POST.get('name')
        addresss = request.POST.get('address')
        snames = request.POST.get('sname')
        phones = request.POST.get('phone')
        faxs = request.POST.get('fax')
        emails = request.POST.get('email')
        bcodes = request.POST.get('bcode')
        if request.method == 'POST' and request.FILES:
            image = request.FILES['logo']
            store = FileSystemStorage()
            filename = store.save(image.name, image)
            profile_pic_url = store.url(filename)
            data=BranchInformationM.objects.get(pk=id)
            data.Company_Name=cname
            data.Name=names
            data.Address=addresss
            data.Short_Name=snames
            data.Phone=phones
            data.Fax=faxs
            data.Email=emails
            data.Branch_Code=bcodes
            data.BranchLogo=filename
            data.save()
        else:
            data = BranchInformationM.objects.get(pk=id)
            data.Company_Name = cname
            data.Name = names
            data.Address = addresss
            data.Short_Name = snames
            data.Phone = phones
            data.Fax = faxs
            data.Email = emails
            data.Branch_Code = bcodes
            data.BranchLogo=ima.BranchLogo
            data.save()
        messages.info(request, 'Update Saved')
        return redirect('/branch/information/')

def branchinfodeleteV(request,id=0):
    if id !=0:
        data=BranchInformationM.objects.get(pk=id)
        data.delete()
        messages.info(request, 'Delete Saved')
    return redirect('/branch/information/')

def createuserV(request):
    company = BranchInformationM.objects.filter(Branch_Code=1)
    companys = BranchInformationM.objects.all()
    return render(request,'admin/forms/createuser.html',{'company':company,'companys':companys})

def createusersaveV(request):
    company = BranchInformationM.objects.filter(Branch_Code=1)
    if request.method == 'POST' and request.FILES:
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        present = request.POST.get('present')
        permanent = request.POST.get('permanent')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        branch_code = request.POST.getlist('branch')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User Name already taken')
                return redirect('/Singup/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'E-Mail already taken')
                return redirect('/Singup/')
            else:
                image = request.FILES['logo']
                store = FileSystemStorage()
                filename = store.save(image.name, image)
                profile_pic_url = store.url(filename)
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                sing = UserProfileM(user=user,Phone=phone, Present_Address=present, Permanant_Address=permanent, Image=filename)
                sing.save()
                c = min([len(branch_code)])
                for i in range(c):
                    users=User.objects.get(pk=request.user.id)
                    Branch=BranchInformationM.objects.get(Branch_Code=branch_code[i])
                    data = UserBranchM.objects.create(User_Id=user, Branch_Code=Branch)
                messages.info(request, 'Data Saved')
                return redirect('/create/user/')
        else:
            messages.info(request, 'password donot match')
            return redirect('/create/user/')
    else:
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        present = request.POST.get('present')
        permanent = request.POST.get('permanent')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        branch_code = request.POST.getlist('branch')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User Name already taken')
                return redirect('/Singup/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'E-Mail already taken')
                return redirect('/Singup/')
            else:

                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                sing = UserProfileM(user=user, Phone=phone, Present_Address=present, Permanant_Address=permanent,
                         )
                sing.save()
                c = min([len(branch_code)])
                for i in range(c):
                    users = User.objects.get(pk=request.user.id)
                    Branch = BranchInformationM.objects.get(Branch_Code=branch_code[i])
                    data = UserBranchM.objects.create(User_Id=user, Branch_Code=Branch)
                messages.info(request, 'Data Saved')
                return redirect('/create/user/')
        else:
            messages.info(request, 'password donot match')
            username = request.POST.get('username')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            present = request.POST.get('present')
            permanent = request.POST.get('permanent')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            branch_code = request.POST.getlist('branch')
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'User Name already taken')
                    return redirect('/Singup/')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'E-Mail already taken')
                    return redirect('/Singup/')
                else:
                    image = request.FILES['logo']
                    store = FileSystemStorage()
                    filename = store.save(image.name, image)
                    profile_pic_url = store.url(filename)
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.save()
                    sing = UserProfileM(user=user, Phone=phone, Present_Address=present, Permanant_Address=permanent,
                                        Image=filename)
                    sing.save()
                    c = min([len(branch_code)])
                    for i in range(c):
                        users = User.objects.get(pk=request.user.id)
                        Branch = BranchInformationM.objects.get(Branch_Code=branch_code[i])
                        data = UserBranchM.objects.create(User_Id=user, Branch_Code=Branch)
                    messages.info(request, 'Data Saved')
                    return redirect('/create/user/')
            else:
                messages.info(request, 'password donot match')
        return render(request,'admin/forms/createuser.html',{'company':company})

def branchselectV(request):
    branch_code = request.POST.get('branch')
    if branch_code:
        if request.method == 'POST':


            data = User.objects.get(id=request.user.id)
            data.last_name=branch_code
            data.save()
    return redirect('/')


