from django.contrib import admin
from .models import indexdb , footerdb, indexselldb
from import_export.admin import ExportActionMixin

class indexdbShow(ExportActionMixin,admin.ModelAdmin):
    list_display = ('base_title', 'base_subtitle')

admin.site.register(indexdb, indexdbShow)
    

class footerdbShow(ExportActionMixin,admin.ModelAdmin):
    list_display = ('my_mail', 'my_tell')

admin.site.register(footerdb, footerdbShow)


class indexselldbShow(ExportActionMixin,admin.ModelAdmin):
    list_display = ('pic_name',)
    
admin.site.register(indexselldb, indexselldbShow)
