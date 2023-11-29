from django.contrib import admin
from .models import Contact



class ContactAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'bus','email', 'image')


    search_fields = ("address",  "phone")
    ordering = ("id", "created_at",)

admin.site.register(Contact, ContactAdmin)