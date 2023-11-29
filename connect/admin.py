from django.contrib import admin
from .models import  Contact



class ContactAdmin(admin.ModelAdmin):
    list_display = ( 'id','f_name', 'l_name', 'email','phone', 'day_time','num_people',
                    'obj_name', 'type_excursion', 'language_excursion', 'created_at')


    search_fields = ("f_name","phone")
    ordering = ("id", "created_at",)



admin.site.register(Contact, ContactAdmin)


