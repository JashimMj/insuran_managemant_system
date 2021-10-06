from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
urlpatterns = [
    path('media/', serve,{'document_root': settings.MEDIA_ROOT}),
    path('static', serve,{'document_root': settings.STATIC_ROOT}),
    path('', views.mainV,name="main"),
    path('', views.indexV, name="index"),
    path('branch/select/', views.branchselectV, name="branchselect"),

    path('main/dashboard/', views.maindashboardV, name="maindashboard"),
    # ---------------------Admin------------------------------
    path('admins/dashboard/', views.admindashboardV, name="admindashboard"),
    # ---------------------------branch info---------------------------
    path('branch/information/', views.branchinfoV, name="branchinfo"),
    path('branch/information/save/', views.branchinfosaveV, name="branchinfosave"),
    path('branch/information/edit/<int:id>/', views.branchinfoeditV, name="branchinfoedit"),
    path('branch/information/update/<int:id>/', views.branchinfoupdateV, name="branchinfoupdate"),
    path('branch/information/delete/<int:id>/', views.branchinfodeleteV, name="branchinfodelete"),
    path('branch/information/report/', views.branchinfoPDFV, name="branchinforeport"),
    # ---------------------------Client info---------------------------
    path('Client/information/', views.clientinfoV, name="client"),
    path('Client/information/save/', views.clientinfosaveV, name="clientsave"),
    path('Client/information/edit/<int:id>', views.clientinfoeditV, name="clientedit"),
    path('Client/information/update/<int:id>', views.clientinfoupdateV, name="clientupdate"),
    path('Client/information/delete/<int:id>', views.clientinfodeleteV, name="clientdelete"),
    path('Client/information/report/', views.clientinfoPDFV, name="clientinfoPDF"),
    # ---------------------------Client Address info---------------------------
    path('Clientaddress/information/', views.clientaddressinfoV, name="clientaddress"),
    path('Clientaddress/information/save/', views.clientaddressinfosaveV, name="clientaddressave"),
    path('Client/address/edit/<int:id>', views.clientaddresseditV, name="clientaddressedit"),
    path('Client/address/update/<int:id>', views.clientaddressupdateV, name="clientaddressupdate"),
    path('Client/address/delete/<int:id>', views.clientaddressdeleteV, name="clientaddressdelete"),
    path('Client/Address/report/', views.clientaddressPDFV, name="clientaddressPDF"),
    # ---------------------------Bank  info---------------------------
    path('bank/information/', views.bankinfoV, name="bank"),
    path('bank/information/save/', views.bankinfosaveV, name="banksave"),
    path('bank/information/edit/<int:id>', views.bankinfoeditV, name="bankedit"),
    path('bank/information/update/<int:id>', views.bankinfoupdateV, name="bankupdate"),
    path('bank/information/delete/<int:id>', views.bankinfodeleteV, name="bankdelete"),
    path('bank/information/report/', views.bankinfoPDFV, name="bankinfoPDF"),
  # ---------------------------bank Address info---------------------------
    path('bankaddress/information/', views.bankaddressinfoV, name="bankaddress"),
    path('bankaddress/information/save/', views.bankaddressinfosaveV, name="bankaddressave"),
    path('bank/address/edit/<int:id>', views.bankaddresseditV, name="bankaddressedit"),
    path('bank/address/update/<int:id>', views.bankaddressupdateV, name="bankaddressupdate"),
    path('bank/address/delete/<int:id>', views.bankaddressdeleteV, name="bankaddressdelete"),
    path('bank/Address/report/', views.bankaddressPDFV, name="bankaddressPDF"),
    #-----------------------Transit By-------------------------------
    path('transit/by/', views.transitV, name="transit"),
    path('transit/by/save/', views.transitsaveV, name="transitsave"),
    path('transit/by/edit/<int:id>', views.transiteditV, name="transitedit"),
    path('transit/by/update/<int:id>', views.transitupdateV, name="transitupdate"),
    path('transit/by/delete/<int:id>', views.transitdeleteV, name="transitdelete"),
    path('transit/by/report/', views.transitPDFV, name="transitpdf"),
    #-----------------------Currency-------------------------------
    path('currency/', views.currencyV, name="currency"),
    path('currency/save/', views.currencysaveV, name="currencysave"),
    path('currency/edit/<int:id>', views.currencyeditV, name="currencyedit"),
    path('currency/update/<int:id>', views.currencyupdateV, name="currencyupdate"),
    path('currency/delete/<int:id>', views.currencydeleteV, name="currencydelete"),
    path('currency/report/', views.currencyPDFV, name="currencypdf"),
    # -----------------------Transit By-------------------------------
    path('Voyage/Via/', views.voyageviaV, name="voyage"),
    path('Voyage/Via/save/', views.voyageviasaveV, name="voyageviasave"),
    path('Voyage/Via/edit/<int:id>', views.voyageeditV, name="voyageedit"),
    path('Voyage/Via/update/<int:id>', views.voyageupdateV, name="voyageupdate"),
    path('Voyage/Via/delete/<int:id>', views.voyagedeleteV, name="voyagedelete"),
    path('Voyage/Via/report/', views.voyagePDFV, name="voyagepdf"),
    # -----------------------------------Create User--------------------
    path('create/user/', views.createuserV, name="createuser"),
    path('create/user/save/', views.createusersaveV, name="createusersave"),
    # -----------------------------------HR--------------------
    path('hr/dashboard/', views.hrdashboarV, name="hrdashboar"),
    # -----------------------------------Employees Info--------------------
    path('employees/info/', views.employeesinfoV, name="employeesinfo"),
    path('employees/info/select', views.employeesinfoselectV, name="employeesinfoselect"),
    path('employees/data/save', views.employeesinfosaveV, name="employeesinfosave"),
    path('employees/data/select2', views.employeesselectV, name="employeesselect"),
    path('employees/calculation/', views.calculationV, name="calculation"),
    #------------------------------Department---------------------------------
    path('Department/info',views.DepartmentV,name='department'),
    path('Department/info/save/',views.DepartmentsaveV,name='departmentsaved'),
    path('Department/info/Edit/<int:id>',views.DepartmenteditV,name='departmentedit'),
    path('Department/info/Update/<int:id>',views.DepartmentUpdateV,name='departmentupdate'),
    path('Department/info/delete/<int:id>',views.DepartmentDeleteV,name='departmentdelete'),
    path('Department/info/PDF/',views.DepertmentPDFV,name='departmentPDF'),
    #------------------------------Designation---------------------------------
    path('Designation/info',views.DesignationV,name='designation'),
    path('Designation/info/save/',views.DesignationsaveV,name='designationsaved'),
    path('Designation/info/Edit/<int:id>',views.DesignationeditV,name='designationedit'),
    path('Designation/info/Update/<int:id>',views.DesignationUpdateV,name='designationupdate'),
    path('Designation/info/delete/<int:id>',views.DesignationDeleteV,name='designationdelete'),
    path('Designation/info/PDF/',views.DesignationPDFV,name='designationPDF'),



    # -----------------------------------Under Writting --------------------
    path('uw/dashboard/', views.uwdashboardV, name="uwdashboard"),
    path('uw/quotation/dashboard/', views.quwdashboardV, name="quwdashboard"),
    path('uw/quotation/marine/', views.qmarineV, name="qmarine"),
    path('uw/quotation/marine/select/client/', views.qmarineselectclientV, name="qmarineselectclient"),
    path('uw/quotation/marine/select/bank/', views.qmarineselectbankV, name="qmarineselectbank"),
    path('uw/quotation/marine/select/bank/add/', views.qmarineselectbankaddV, name="qmarineselectbankadd"),
    path('uw/quotation/marine/enddate/', views.qmarinedateV, name="qmarinesendate"),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
