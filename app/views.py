# Create your views here.

from django.shortcuts import render
from app.models import Estudiante

def home(request):
	estudiantes = Estudiante.objects.all()
	return render(request, 'home.html' , {"estudiantes":estudiantes})

