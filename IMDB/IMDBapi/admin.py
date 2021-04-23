from django.contrib import admin
from .models import IMDBdata
# Register your models here.

class IMDBdataAdmin(admin.ModelAdmin):
    pass

admin.site.register(IMDBdata,IMDBdataAdmin)