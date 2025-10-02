from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView,DeleteView, DetailView
from .models import Tarea
from .forms import TareaForm


# Create your views here.
class TareaListView(ListView):
    model = Tarea
    template_name = "tarea/tarea_list.html"
    context_object_name = "tareas"

class TareaCreateView(CreateView):
    model = Tarea
    form_class = TareaForm
    # fields = ["titulo", "descripcion", "prioridad", "vigente", "fecha_limite"]
    template_name = "tarea/tarea_form.html"
    success_url = reverse_lazy("tareas:lista")

class TareaDetailView(DetailView):
    model = Tarea
    template_name = "tarea/tarea_detail.html"
    context_object_name = "tarea"

class TareaUpdateView(UpdateView):
    model = Tarea
    fields = ["titulo", "descripcion", "prioridad", "vigente", "fecha_limite"]
    template_name = "tarea/tarea_form.html"
    success_url = reverse_lazy("tareas:lista")

class TareaDeleteView(DeleteView):
    model = Tarea
    template_name = "tarea/tarea_confirm_delete.html"
    success_url = reverse_lazy("tareas:lista")


# class SectorCreateView(CreateView):
# model = Sector
# fields = ["nombre"]
# template_name = "huertos/sector_form.html"
# success_url = reverse_lazy("sector:lista")