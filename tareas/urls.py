from django.urls import path
from . import views

app_name="tareas"

urlpatterns = [
    path('', views.TareaListView.as_view(), name="lista"),
]
