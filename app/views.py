# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("Ola k ase")
