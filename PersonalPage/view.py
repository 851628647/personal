from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render


def index(request):
    context = {}
    context['hello'] = "hello world"
    return render(request, 'keep.html', context)
