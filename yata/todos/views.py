from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world")

from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def index(request):

    return render(request, "todos/index.html")