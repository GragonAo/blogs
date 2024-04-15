
# Register your models here.
from django.contrib import admin
from .models import User
class UserAdmin(admin.ModelAdmin):
# list_display表示要显示哪些属性
    list_display = ['id','username','password','email','create_time']
admin.site.register(User,UserAdmin)