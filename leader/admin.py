from django.contrib import admin
from .models import Leader




class LeaderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'about', 'image', 'number', 'email')

    list_filter = ('name',)
    search_fields = ("id","name")



admin.site.register(Leader, LeaderAdmin)
