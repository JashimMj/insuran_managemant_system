from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .resources import CurrencyResource

class BookAdmin(ImportExportModelAdmin):
    resource_class = CurrencyResource
admin.site.register(Currency, BookAdmin)
admin.site.register(BranchInformationM)
admin.site.register(UserBranchM)
admin.site.register(EmployeesinfoM)
admin.site.register(UserProfileM)
