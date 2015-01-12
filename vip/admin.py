from django.contrib import admin
from vip.models import User
from vip.models import GlobVar
# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = ('username','password','email','available_days','balance','rechargetime')

class GlobVarAdmin(admin.ModelAdmin):
	list_display = ('autosubavday','currentfg')

admin.site.register(User,UserAdmin)
admin.site.register(GlobVar,GlobVarAdmin)