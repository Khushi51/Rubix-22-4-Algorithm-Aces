from django.contrib import admin

# Register your models here.
from .models import LabBilling, LabTests

admin.site.register(LabTests)
admin.site.register(LabBilling)
