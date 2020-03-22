from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Role

def index(request, id):
    roles = Role.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    return render(request, 'index.html', {'roles':roles})


# roles = get_object_or_404(Role, pk=id)

# from django.http import HttpResponse

# def index(request, id):
#     return HttpResponse("Hello, world!")