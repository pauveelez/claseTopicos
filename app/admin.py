from django.contrib import admin
from .models import Estudiante, Carrera

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'imagen_rosada', 'email', 'telefono', 'carrera','es_informatico')
    list_editable = ('email', 'telefono', 'carrera', )
    #list_display_links = ('carrera',)
    list_filter = ('carrera',)
    search_fields = ('carrera__nombre', 'nombre')

    raw_id_fields = ('carrera',)

    def imagen_rosada(self, obj):
        url = obj.dar_imagen_nombre_rosada()
        tag = '<img src="%s"/>' % url
        return tag
    imagen_rosada.allow_tags = True
    imagen_rosada.admin_order_field = 'carrera'

class EstudianteInline(admin.StackedInline):
    model = Estudiante
    extra = 1

class CarreraAdmin(admin.ModelAdmin):
    inlines = [EstudianteInline]

admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Carrera, CarreraAdmin)
