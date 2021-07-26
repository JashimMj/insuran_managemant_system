from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
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
    # -----------------------------------Create User--------------------
    path('create/user/', views.createuserV, name="createuser"),
    path('create/user/save/', views.createusersaveV, name="createusersave"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
