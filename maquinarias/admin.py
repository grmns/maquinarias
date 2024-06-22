from django.contrib import admin
from .models import Maquinaria

@admin.register(Maquinaria)
class MaquinariaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion')
