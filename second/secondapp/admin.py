from django.contrib import admin
from secondapp.models import ContactApp


class contactAdmin(admin.ModelAdmin):
    list_display=('name','surname','phone','email','password')

admin.site.register(ContactApp,contactAdmin)
