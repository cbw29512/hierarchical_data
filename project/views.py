from django.shortcuts import render
from django.http import HttpResponse
from project.models import Tree
# Create your views here.


def project_list(request):
    return render(request, 'index.html', {'tree': Tree.objects.all()})
