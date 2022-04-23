from django.contrib import admin
from .models import karbaruser
from import_export.admin import ExportActionMixin



class karbarusershow(ExportActionMixin,admin.ModelAdmin):
    list_display = ('username', 'email','tell',)
    search_fields = ('username',)
   

admin.site.register(karbaruser, karbarusershow)