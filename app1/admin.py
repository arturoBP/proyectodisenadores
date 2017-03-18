from django.contrib import admin
from .models import autorModel

class AutorAdmin(admin.ModelAdmin):
    pass

admin.site.register(autorModel, AutorAdmin)


# Register your models here.
