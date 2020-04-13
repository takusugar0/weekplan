from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/tasks', views.index, name='tasks.index'),
    path('<int:id>/tasks/create', views.create_task, name='tasks.create'),
    path('create', views.create_role, name='roles.create'),
    path('<int:id>/tasks/<int:task_id>', views.edit_task, name='tasks.edit'),
]