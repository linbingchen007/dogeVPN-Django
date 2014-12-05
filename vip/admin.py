from django.contrib import admin
from vip.models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = ('username','password','email','available_days','balance')

admin.site.register(User,UserAdmin)