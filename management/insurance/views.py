from django.shortcuts import render,redirect
from django.contrib import auth,messages
from django.core.files.storage import FileSystemStorage
from .models import *
from django.http import HttpResponseRedirect
# Create your views here.
## PDF CODE ###
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import datetime
from django.http import JsonResponse




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
    currentbranch = BranchInformationM.objects.raw(
        'select a.id,a.Name from insurance_branchinformationm a,auth_user b where b.id=%s and a.branch_code=b.last_name',
        [request.user.id])
    ubranch = UserBranchM.objects.filter(User_Id=request.user.id)
    company = BranchInformationM.objects.filter(Branch_Code=1)

    return render(request,'pages/maindashboard.html',{'company':company,'ubranch':ubranch,'currentbranch':currentbranch})


def admindashboardV(request):
    currentbranch = BranchInformationM.objects.raw(
        'select a.id,a.Name from insurance_branchinformationm a,auth_user b where b.id=%s and a.branch_code=b.last_name',
        [request.user.id])
    ubranch = UserBranchM.objects.filter(User_Id=request.user.id)
    company = BranchInformationM.objects.filter(Branch_Code=1)
    return render(request,'admin/admindashboard.html',{'company':company,'ubranch':ubranch,'currentbranch':currentbranch})


def hrdashboarV(request):
    currentbranch = BranchInformationM.objects.raw(
        'select a.id,a.Name from insurance_branchinformationm a,auth_user b where b.id=%s and a.branch_code=b.last_name',
        [request.user.id])
    ubranch = UserBranchM.objects.filter(User_Id=request.user.id)
    company = BranchInformationM.objects.filter(Branch_Code=1)
    return render(request,'hr/hrdashboard.html',{'company':company,'ubranch':ubranch,'currentbranch':currentbranch})


def branchinfoV(request):
    currentbranch = BranchInformationM.objects.raw(
        'select a.id,a.Name from insurance_branchinformationm a,auth_user b where b.id=%s and a.branch_code=b.last_name',
        [request.user.id])
    ubranch = UserBranchM.objects.filter(User_Id=request.user.id)
    company = BranchInformationM.objects.filter(Branch_Code=1)
    companys = BranchInformationM.objects.all()
    return render(request,'admin/forms/branchinfo.html',{'company':company,'companys':companys,'ubranch':ubranch,'currentbranch':currentbranch})

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
    currentbranch = BranchInformationM.objects.raw(
        'select a.id,a.Name from insurance_branchinformationm a,auth_user b where b.id=%s and a.branch_code=b.last_name',
        [request.user.id])
    ubranch = UserBranchM.objects.filter(User_Id=request.user.id)
    company = BranchInformationM.objects.filter(Branch_Code=1)
    companys = BranchInformationM.objects.all()
    if id != 0:
        companyedit = BranchInformationM.objects.filter(pk=id)
    return render(request,'admin/forms/branchinfoedit.html',{'company':company,'companyedit':companyedit,'companys':companys,'ubranch':ubranch,'currentbranch':currentbranch})


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
    currentbranch = BranchInformationM.objects.raw(
        'select a.id,a.Name from insurance_branchinformationm a,auth_user b where b.id=%s and a.branch_code=b.last_name',
        [request.user.id])
    ubranch = UserBranchM.objects.filter(User_Id=request.user.id)
    company = BranchInformationM.objects.filter(Branch_Code=1)
    companys = BranchInformationM.objects.all()
    return render(request,'admin/forms/createuser.html',{'company':company,'companys':companys,'ubranch':ubranch,'currentbranch':currentbranch})

def createusersaveV(request):
    currentbranch = BranchInformationM.objects.raw(
        'select a.id,a.Name from insurance_branchinformationm a,auth_user b where b.id=%s and a.branch_code=b.last_name',
        [request.user.id])
    ubranch = UserBranchM.objects.filter(User_Id=request.user.id)
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
        return render(request,'admin/forms/createuser.html',{'company':company,'ubranch':ubranch,'currentbranch':currentbranch})

def branchselectV(request):
    branch_code = request.POST.get('branch')
    if branch_code:
        if request.method == 'POST':


            data = User.objects.get(id=request.user.id)
            data.last_name=branch_code
            data.save()
    return redirect('/')

def employeesinfoV(request):
    currentbranch = BranchInformationM.objects.raw('select a.id,a.Name from insurance_branchinformationm a,auth_user b where b.id=%s and a.branch_code=b.last_name',[request.user.id])
    company = BranchInformationM.objects.filter(Branch_Code=1)
    ubranch = UserBranchM.objects.filter(User_Id=request.user.id)
    return render(request,'hr/forms/employeesinfo.html',{'ubranch':ubranch,'company':company,'currentbranch':currentbranch})


def branchinfoPDFV(request):
    company = BranchInformationM.objects.filter(Branch_Code=1)
    branch=BranchInformationM.objects.all()
    template_path = 'admin/report/branchinfoPDF.html'
    context = {'company':company,'branch':branch}
    response = HttpResponse(content_type='application/pdf')
    # for downlode
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def uwdashboardV(request):
    currentbranch = BranchInformationM.objects.raw(
        'select a.id,a.Name from insurance_branchinformationm a,auth_user b where b.id=%s and a.branch_code=b.last_name',
        [request.user.id])
    company = BranchInformationM.objects.filter(Branch_Code=1)
    ubranch = UserBranchM.objects.filter(User_Id=request.user.id)
    return render(request,'underwritting/uwdashboard.html',{'currentbranch':currentbranch,'company':company,'ubranch':ubranch})


def quwdashboardV(request):
    currentbranch = BranchInformationM.objects.raw(
        'select a.id,a.Name from insurance_branchinformationm a,auth_user b where b.id=%s and a.branch_code=b.last_name',
        [request.user.id])
    company = BranchInformationM.objects.filter(Branch_Code=1)
    ubranch = UserBranchM.objects.filter(User_Id=request.user.id)
    return render(request,'underwritting/quwdashboard.html',{'currentbranch':currentbranch,'company':company,'ubranch':ubranch})



def clientinfoV(request):
    client=ClientInformation.objects.all()
    currentbranch = BranchInformationM.objects.raw('select a.id,a.Name from insurance_branchinformationm a,auth_user b where b.id=%s and a.branch_code=b.last_name',[request.user.id])
    company = BranchInformationM.objects.filter(Branch_Code=1)
    ubranch = UserBranchM.objects.filter(User_Id=request.user.id)
    return render(request, 'admin/forms/cliententry.html',{'currentbranch': currentbranch, 'company': company, 'ubranch': ubranch,'client':client})

def clientinfosaveV(request):
    if request.method == 'POST':
        Cname=request.POST.get('cname')
        currentbranch = BranchInformationM.objects.raw(
            'select a.id,a.Name from insurance_branchinformationm a,auth_user b where b.id=%s and a.branch_code=b.last_name',
            [request.user.id])
        for x in currentbranch:
            dbrance=BranchInformationM.objects.get(id=x.id)
            data = ClientInformation.objects.create(Client_Name=Cname,branch=dbrance)
            messages.info(request, 'Client Save')
    else:
        messages.info(request, 'Client Do Not Saved')
    return redirect('/Client/information/')

def clientinfoeditV(request,id=0):
    currentbranch = BranchInformationM.objects.raw(
        'select a.id,a.Name from insurance_branchinformationm a,auth_user b where b.id=%s and a.branch_code=b.last_name',
        [request.user.id])
    company = BranchInformationM.objects.filter(Branch_Code=1)
    ubranch = UserBranchM.objects.filter(User_Id=request.user.id)
    if id !=0:
        data=ClientInformation.objects.get(id=id)
    return render(request, 'admin/forms/cliententryedit.html',{'currentbranch': currentbranch, 'company': company, 'ubranch': ubranch,'data':data})

def clientinfoupdateV(request,id=0):
    clientname=request.POST.get('cname')
    if id !=0:
        data = ClientInformation.objects.get(id=id)
        data.Client_Name=clientname
        data.save()
        messages.info(request, 'Client Update')
    return redirect('/Client/information/')


def clientinfoPDFV(request):
    company = BranchInformationM.objects.filter(Branch_Code=1)
    Client=ClientInformation.objects.all()
    template_path = 'admin/report/ClientinfoPDF.html'
    context = {'company':company,'Client':Client}
    response = HttpResponse(content_type='application/pdf')
    # for downlode
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def clientinfodeleteV(request,id=0):
    if id !=0:
        data = ClientInformation.objects.get(id=id)
        data.delete()
        messages.info(request, 'Client Deleted')
    return redirect('/Client/information/')


def clientaddressinfoV(request):
    currentbranch = BranchInformationM.objects.raw(
        'select a.id,a.Name from insurance_branchinformationm a,auth_user b where b.id=%s and a.branch_code=b.last_name',
        [request.user.id])
    company = BranchInformationM.objects.filter(Branch_Code=1)
    ubranch = UserBranchM.objects.filter(User_Id=request.user.id)
    client = ClientInformation.objects.all()
    clients = ClentAddressInformation.objects.all()
    return render(request, 'admin/forms/clientaddressentry.html',{'currentbranch': currentbranch, 'company': company, 'ubranch': ubranch,'clients':clients,'client':client})

def clientaddressinfosaveV(request):
    if request.method=='POST':
        clinetname=request.POST.get('cname')
        caddress=request.POST.get('address')
        cphone=request.POST.get('phone')
        cemail=request.POST.get('email')

        cclinet=ClientInformation.objects.get(id=clinetname)
        data=ClentAddressInformation.objects.create(Client_Name=cclinet,Address=caddress,Phone=cphone,Email=cemail)
        messages.info(request, 'Client Address Save')
    else:
        messages.info(request, 'Client Address Do not Saved')
    return redirect('/Clientaddress/information/')


def clientaddresseditV (request,id=0):
    client = ClientInformation.objects.all()
    clients = ClentAddressInformation.objects.all()
    currentbranch = BranchInformationM.objects.raw(
        'select a.id,a.Name from insurance_branchinformationm a,auth_user b where b.id=%s and a.branch_code=b.last_name',
        [request.user.id])
    company = BranchInformationM.objects.filter(Branch_Code=1)
    ubranch = UserBranchM.objects.filter(User_Id=request.user.id)
    if id != 0:
        data = ClentAddressInformation.objects.get(id=id)
    return render(request, 'admin/forms/clientaddressedit.html',
                  {'currentbranch': currentbranch, 'company': company, 'ubranch': ubranch, 'data': data,'client':client,'clients':clients})




def clientaddressupdateV(request,id=0):
    clientname=request.POST.get('cname')
    caddres=request.POST.get('address')
    cphone=request.POST.get('phone')
    cemail=request.POST.get('email')
    cclients=ClientInformation.objects.get(id=clientname)
    if id !=0:
        data = ClentAddressInformation.objects.get(id=id)
        data.Client_Name=cclients
        data.Address=caddres
        data.Phone=cphone
        data.Email=cemail
        data.save()
        messages.info(request, 'Client Update')
    return redirect('/Clientaddress/information/')



def clientaddressdeleteV(request,id=0):
    if id !=0:
        data = ClentAddressInformation.objects.get(id=id)
        data.delete()
        messages.info(request, 'Client Deleted')
    return redirect('/Clientaddress/information/')


def clientaddressPDFV(request):
    company = BranchInformationM.objects.filter(Branch_Code=1)
    Client=ClentAddressInformation.objects.all()
    template_path = 'admin/report/ClientaddressPDF.html'
    context = {'company':company,'Client':Client}
    response = HttpResponse(content_type='application/pdf')
    # for downlode
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def bankinfoV(request):
    bank = Bankinformation.objects.all()
    currentbranch = BranchInformationM.objects.raw(
        'select a.id,a.Name from insurance_branchinformationm a,auth_user b where b.id=%s and a.branch_code=b.last_name',
        [request.user.id])
    company = BranchInformationM.objects.filter(Branch_Code=1)
    ubranch = UserBranchM.objects.filter(User_Id=request.user.id)
    return render(request, 'admin/forms/bankentry.html',
                  {'currentbranch': currentbranch, 'company': company, 'ubranch': ubranch, 'bank': bank})



def bankinfosaveV(request):
    if request.method == 'POST':
        Cname=request.POST.get('cname')
        currentbranch = BranchInformationM.objects.raw(
            'select a.id,a.Name from insurance_branchinformationm a,auth_user b where b.id=%s and a.branch_code=b.last_name',
            [request.user.id])
        for x in currentbranch:
            dbrance=BranchInformationM.objects.get(id=x.id)
            data = Bankinformation.objects.create(Bank_Name=Cname,branch=dbrance)
            messages.info(request, 'Bank Save')
    else:
        messages.info(request, 'Bank Do Not Saved')
    return redirect('/bank/information/')


def bankinfoeditV(request,id=0):
    currentbranch = BranchInformationM.objects.raw(
        'select a.id,a.Name from insurance_branchinformationm a,auth_user b where b.id=%s and a.branch_code=b.last_name',
        [request.user.id])
    company = BranchInformationM.objects.filter(Branch_Code=1)
    ubranch = UserBranchM.objects.filter(User_Id=request.user.id)
    if id !=0:
        data=Bankinformation.objects.get(id=id)
    return render(request, 'admin/forms/bankentryedit.html',{'currentbranch': currentbranch, 'company': company, 'ubranch': ubranch,'data':data})


def bankinfoupdateV(request,id=0):
    clientname=request.POST.get('cname')
    if id !=0:
        data = Bankinformation.objects.get(id=id)
        data.Bank_Name=clientname
        data.save()
        messages.info(request, 'Bank Update')
    return redirect('/bank/information/')


def bankinfoPDFV(request):
    company = BranchInformationM.objects.filter(Branch_Code=1)
    Client=Bankinformation.objects.all()
    template_path = 'admin/report/bankinfoPDF.html'
    context = {'company':company,'Client':Client}
    response = HttpResponse(content_type='application/pdf')
    # for downlode
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def bankinfodeleteV(request,id=0):
    if id !=0:
        data = Bankinformation.objects.get(id=id)
        data.delete()
        messages.info(request, 'Bank Deleted')
    return redirect('/bank/information/')

def bankaddressinfoV(request):
    currentbranch = BranchInformationM.objects.raw(
        'select a.id,a.Name from insurance_branchinformationm a,auth_user b where b.id=%s and a.branch_code=b.last_name',
        [request.user.id])
    company = BranchInformationM.objects.filter(Branch_Code=1)
    ubranch = UserBranchM.objects.filter(User_Id=request.user.id)
    bank = Bankinformation.objects.all()
    banks = BankBranch.objects.all()
    return render(request, 'admin/forms/bankaddressentry.html',{'currentbranch': currentbranch, 'company': company, 'ubranch': ubranch,'banks':banks,'bank':bank})

def bankaddressinfosaveV(request):
    if request.method=='POST':
        clinetname=request.POST.get('cname')
        caddress=request.POST.get('address')
        branch=request.POST.get('branchs')
        cphone=request.POST.get('phone')
        cemail=request.POST.get('email')

        cclinet=Bankinformation.objects.get(id=clinetname)
        data=BankBranch.objects.create(Bank_Name=cclinet,Address=caddress,Phone=cphone,Email=cemail,Branch_Name=branch)
        messages.info(request, 'Client Address Save')
    else:
        messages.info(request, 'Bank Address Do not Saved')
    return redirect('/bankaddress/information/')


def bankaddresseditV (request,id=0):
    bank = Bankinformation.objects.all()
    banks = Bankinformation.objects.all()
    currentbranch = BranchInformationM.objects.raw(
        'select a.id,a.Name from insurance_branchinformationm a,auth_user b where b.id=%s and a.branch_code=b.last_name',
        [request.user.id])
    company = BranchInformationM.objects.filter(Branch_Code=1)
    ubranch = UserBranchM.objects.filter(User_Id=request.user.id)
    if id != 0:
        data = BankBranch.objects.get(id=id)
    return render(request, 'admin/forms/bankaddressedit.html',
                  {'currentbranch': currentbranch, 'company': company, 'ubranch': ubranch, 'data': data,'bank':bank,'banks':banks})


def bankaddressupdateV(request,id=0):
    clientname=request.POST.get('cname')
    caddres=request.POST.get('address')
    cphone=request.POST.get('phone')
    cemail=request.POST.get('email')
    branchs=request.POST.get('branch')
    cclients=Bankinformation.objects.get(id=clientname)
    if id !=0:
        data = BankBranch.objects.get(id=id)
        data.Client_Name=cclients
        data.Branch_Name=branchs
        data.Address=caddres
        data.Phone=cphone
        data.Email=cemail
        data.save()
        messages.info(request, 'Bank Update')
    return redirect('/bankaddress/information/')

def bankaddressdeleteV(request,id=0):
    if id !=0:
        data = BankBranch.objects.get(id=id)
        data.delete()
        messages.info(request, 'Bank Deleted')
    return redirect('/bankaddress/information/')


def bankaddressPDFV(request):
    company = BranchInformationM.objects.filter(Branch_Code=1)
    bank=BankBranch.objects.all()
    template_path = 'admin/report/bankaddressPDF.html'
    context = {'company':company,'bank':bank}
    response = HttpResponse(content_type='application/pdf')
    # for downlode
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def transitV(request):
    transit = TransitBy.objects.all()
    currentbranch = BranchInformationM.objects.raw(
        'select a.id,a.Name from insurance_branchinformationm a,auth_user b where b.id=%s and a.branch_code=b.last_name',
        [request.user.id])
    company = BranchInformationM.objects.filter(Branch_Code=1)
    ubranch = UserBranchM.objects.filter(User_Id=request.user.id)
    return render(request,'admin/forms/transit.html',{'transit':transit,'currentbranch':currentbranch,'company':company,'ubranch':ubranch})
def transitsaveV(request):
    if request.method == 'POST':
        trans = request.POST.get('transit')

        data = TransitBy.objects.create(name=trans)
        messages.info(request, 'Data Save')
    else:
        messages.info(request, 'Data Do Not Saved')
    return redirect('/transit/by/')

def transiteditV (request,id=0):
    currentbranch = BranchInformationM.objects.raw(
        'select a.id,a.Name from insurance_branchinformationm a,auth_user b where b.id=%s and a.branch_code=b.last_name',
        [request.user.id])
    company = BranchInformationM.objects.filter(Branch_Code=1)
    ubranch = UserBranchM.objects.filter(User_Id=request.user.id)
    if id != 0:
        data = TransitBy.objects.get(id=id)
    return render(request, 'admin/forms/transitedit.html',
                  {'currentbranch': currentbranch, 'company': company, 'ubranch': ubranch,'data':data})

def transitupdateV(request,id=0):
    trans=request.POST.get('transit')
    if id !=0:
        data = TransitBy.objects.get(id=id)
        data.name=trans
        data.save()
        messages.info(request, 'Data Update')
    return redirect('/transit/by/')

def transitdeleteV(request,id=0):
    if id !=0:
        data = TransitBy.objects.get(id=id)
        data.delete()
        messages.info(request, 'data Deleted')
    return redirect('/transit/by/')

def transitPDFV(request):
    company = BranchInformationM.objects.filter(Branch_Code=1)
    transit=TransitBy.objects.all()
    template_path = 'admin/report/transitPDF.html'
    context = {'company':company,'transit':transit}
    response = HttpResponse(content_type='application/pdf')
    # for downlode
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def voyageviaV(request):
    voyage = VoyageVia.objects.all()
    currentbranch = BranchInformationM.objects.raw(
        'select a.id,a.Name from insurance_branchinformationm a,auth_user b where b.id=%s and a.branch_code=b.last_name',
        [request.user.id])
    company = BranchInformationM.objects.filter(Branch_Code=1)
    ubranch = UserBranchM.objects.filter(User_Id=request.user.id)
    return render(request,'admin/forms/voyagevia.html',{'voyage':voyage,'currentbranch':currentbranch,'company':company,'ubranch':ubranch})


def voyageviasaveV(request):
    if request.method == 'POST':
        voyag = request.POST.get('voyage')

        data = VoyageVia.objects.create(name=voyag)
        messages.info(request, 'Data Save')
    else:
        messages.info(request, 'Data Do Not Saved')
    return redirect('/Voyage/Via/')

def voyageeditV (request,id=0):
    currentbranch = BranchInformationM.objects.raw(
        'select a.id,a.Name from insurance_branchinformationm a,auth_user b where b.id=%s and a.branch_code=b.last_name',
        [request.user.id])
    company = BranchInformationM.objects.filter(Branch_Code=1)
    ubranch = UserBranchM.objects.filter(User_Id=request.user.id)
    if id != 0:
        data = VoyageVia.objects.get(id=id)
    return render(request, 'admin/forms/Voyageviaedit.html',
                  {'currentbranch': currentbranch, 'company': company, 'ubranch': ubranch,'data':data})


def voyageupdateV(request,id=0):
    voya=request.POST.get('voyage')
    if id !=0:
        data = VoyageVia.objects.get(id=id)
        data.name=voya
        data.save()
        messages.info(request, 'Data Update')
    return redirect('/Voyage/Via/')

def voyagedeleteV(request,id=0):
    if id !=0:
        data = VoyageVia.objects.get(id=id)
        data.delete()
        messages.info(request, 'data Deleted')
    return redirect('/Voyage/Via/')

def voyagePDFV(request):
    company = BranchInformationM.objects.filter(Branch_Code=1)
    voya=VoyageVia.objects.all()
    template_path = 'admin/report/voyagePDF.html'
    context = {'company':company,'voya':voya}
    response = HttpResponse(content_type='application/pdf')
    # for downlode
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def qmarineV(request):
    currentbranch = BranchInformationM.objects.raw(
        'select a.id,a.Name from insurance_branchinformationm a,auth_user b where b.id=%s and a.branch_code=b.last_name',
        [request.user.id])
    company = BranchInformationM.objects.filter(Branch_Code=1)
    ubranch = UserBranchM.objects.filter(User_Id=request.user.id)
    for x in currentbranch:
        dbrance = BranchInformationM.objects.get(id=x.id)
        Client = ClientInformation.objects.filter(branch=dbrance)
        Bank = Bankinformation.objects.filter(branch=dbrance)
        address=ClentAddressInformation.objects.all()
        transit=TransitBy.objects.all()
        voya=VoyageVia.objects.all()
        dases=datetime.datetime.now()
        dases=datetime.datetime.strftime(dases,'%Y-%m-%d')

    return render(request, 'underwritting/forms/marine.html',
                  {'currentbranch': currentbranch, 'company': company,'ubranch': ubranch,
                    'Client': Client, 'Bank': Bank,'address':address,'transit':transit,'voya':voya,'dases':dases})

def qmarineselectclientV(request):
    cname = request.GET.get('cnames')
    caddress=ClentAddressInformation.objects.filter(Client_Name=cname)
    # return render(request,'selectlist/clientaddresslist.html',{'caddress':caddress})
    return JsonResponse({'caddress':list(caddress.values())})

def qmarineselectbankV(request):
    bname = request.GET.get('bnames')
    bbranch=BankBranch.objects.filter(Bank_Name=bname)
    return render(request,'selectlist/bankbranchlist.html',{'bbranch':bbranch})

def qmarineselectbankaddV(request):
    badd = request.GET.get('baddress')
    baddress=BankBranch.objects.filter(Bank_Name=badd)
    return render(request,'selectlist/bankaddresslist.html',{'baddress':baddress})


def qmarinedateV(request):
    fdates = request.GET.get('fdates')
    datess=datetime.datetime.strptime(fdates,'%Y-%m-%d')
    delta = (datess + datetime.timedelta(days=364)).date()
    # return render(request,'selectlist/dates.html',{'delta':delta})
    data={
        'taken':delta
    }

    return JsonResponse({"data":data})




