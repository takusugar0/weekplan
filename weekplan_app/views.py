from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Role, Task
from .forms import RoleForm, TaskForm

def index(request, id):
    #すべてのフォルダを取得する
    roles = Role.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    #選ばれたフォルダを取得する
    current_role = get_object_or_404(Role, id=id)
    #選ばれたフォルダのタスクを取得する
    tasks = Task.objects.filter(role_id = current_role.id)

    return render(request, 'index.html', {
        'roles':roles,
        'tasks':tasks,
        'current_role_id': current_role.id,
    })

def create_role(request):
    if request.method == "POST":
        form = RoleForm(request.POST)
        if form.is_valid():
            role = form.save(commit=False)
            role.created_at = timezone.now()
            role.save()
            return redirect('tasks.index', id=role.id)
    else:
        form = RoleForm()
    return render(request, 'create_roles.html', {'form': form})

def create_task(request, id):
    #選ばれたフォルダを取得する
    current_role = get_object_or_404(Role, id=id)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_at = timezone.now()
            task.role_id = current_role
            task.save()
            return redirect('tasks.index', id=current_role.id)
    else:
        form = TaskForm()
    return render(request, 'create_tasks.html', {'form': form}, {'id':current_role.id})

def edit_task(request, id, task_id):
    #選ばれたタスクを取得する
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('tasks.index', id=task.role_id.id)
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit.html', {'form': form}, {'task':task})

# roles = get_object_or_404(Role, pk=id)

# from django.http import HttpResponse

# def index(request, id):
#     return HttpResponse("Hello, world!")