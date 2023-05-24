from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import anwserTable
 
admin.site.register(anwserTable)
 
admin.site.site_header = '后台管理系统'
admin.site.site_title = '后台管理系统'