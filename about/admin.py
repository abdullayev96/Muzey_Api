from django.contrib import admin
from .models import *


class JobAdmin(admin.ModelAdmin):
    list_display = ('id','job', 'full_name', 'image', 'phone', 'email')

    list_filter = ('full_name',)
    search_fields = ("id","full_name")



admin.site.register(About)
admin.site.register(Structure)
admin.site.register(Img)
admin.site.register(Leader, JobAdmin)




