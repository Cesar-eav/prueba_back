from django.contrib import admin
from .models import Tarea

# Register your models here.

@admin.register(Tarea)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("titulo", "prioridad", "vigente", "fecha_limite", "fecha_creacion")
    search_fields = ("titulo","descripcion")
    list_filter = ("prioridad", "vigente")






