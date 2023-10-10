from django.contrib import admin
from mysqlapp.models import signupModel
from mysqlapp.models import loginModel
# Register your models here.


class signupAdmin(admin.ModelAdmin):
    list_display=("name", "email", "password", )


class loginAdmin(admin.ModelAdmin):
    list_display=("name", "password",)

admin.site.register(signupModel,signupAdmin)
admin.site.register(loginModel,loginAdmin)
