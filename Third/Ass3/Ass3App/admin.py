from django.contrib import admin
from Ass3App.models import loginModel,registerModel
# Register your models here.

class LoginAdmin(admin.ModelAdmin):
    list_display=('email','password')

class RegisterAdmin(admin.ModelAdmin):
    list_display=('name','email','password')

admin.site.register(loginModel,LoginAdmin)
admin.site.register(registerModel,RegisterAdmin)
