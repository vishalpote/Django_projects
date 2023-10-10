from django.contrib import admin
from secondoneapp.models import secondoneappModules


class secondoneappAdmin(admin.ModelAdmin):
    list_display=('title','sec_desc')


admin.site.register(secondoneappModules,secondoneappAdmin)
# Register your models here.
