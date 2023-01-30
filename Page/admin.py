from django.contrib import admin
from Page.models import Form

# Register your models here.
class FormAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','password')
admin.site.register(Form,FormAdmin)
