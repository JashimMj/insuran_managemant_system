from import_export import resources
from .models import *

class CurrencyResource(resources.ModelResource):

    class Meta:
        model = Currency
        fields='id,name'



