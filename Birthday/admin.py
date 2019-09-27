from django.contrib import admin
from Birthday.models import Birth
# Register your models here.
class BirthAdmin(admin.ModelAdmin):
    list_display=['user','email','phone_number','first_name','last_name','birthday']


admin.site.register(Birth,BirthAdmin)