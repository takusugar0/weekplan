from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/tasks', views.index, name='tasks.index'),
]