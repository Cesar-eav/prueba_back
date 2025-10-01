from django.contrib import admin
from .models import Tarea

# Register your models here.

@admin.register(Tarea)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo',)