# Create your views here.

from django.shortcuts import render
from app.models import estudiante

def home(request):
	estudiantes = estudiante.objects.all()
	return render(request, 'home.html' , {"estudiantes":estudiantes})

