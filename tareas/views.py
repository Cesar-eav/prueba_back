from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView,DeleteView
from .models import Tarea

# Create your views here.
class TareaListView(ListView):
    model = Tarea
    template_name = "tarea/lista.html"
    context_object_name = "tareas"

class TareaCreateView(CreateView):
    model = Tarea
    fields = ["titulo", "descripcion", "prioridad", "vigente", "fecha_limite"]
    template_name = "tarea/form.html"
    success_url = reverse_lazy("tareas:lista")

class TareaUpdateView(UpdateView):
    model = Tarea
    fields = ["titulo", "descripcion", "prioridad", "vigente", "fecha_limite"]
    template_name = "tarea/form.html"
    success_url = reverse_lazy("tareas:lista")

class TareaDeleteView(DeleteView):
    model = Tarea
    template_name = "tarea/confirmar_eliminar.html"
    success_url = reverse_lazy("tarea_lista")


# class SectorCreateView(CreateView):
# model = Sector
# fields = ["nombre"]
# template_name = "huertos/sector_form.html"
# success_url = reverse_lazy("sector:lista")