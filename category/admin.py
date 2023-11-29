from django.contrib import admin
from .models import *

class ExhibitAdmin(admin.ModelAdmin):
     list_display = ['id', 'name', 'year', 'category','task', 'body', 'image',
                     'file', 'image_one', 'created_at']



     search_fields = ("name", "task")
     ordering = ("id", "created_at",)


admin.site.register(Exhibit, ExhibitAdmin)
admin.site.register(Category)

