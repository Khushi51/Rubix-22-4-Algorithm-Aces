from django.contrib import admin
from .models import Appointment,Patient


# @admin.register(Appointment)
# class AppoinmentAdmin(admin.ModelAdmin):
#     list_display = ['name', 'email', 'phone', 'doctor', 'date', 'time']
#     date_hierarchy = ('date')
#     list_filter = ['date', 'doctor', ]
#     list_per_page = 20
#     search_fields = ['doctor', 'name', ]

admin.site.register(Appointment)
admin.site.register(Patient)