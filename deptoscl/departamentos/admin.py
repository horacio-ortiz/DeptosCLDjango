from django.contrib import admin

# Register your models here.
from .models import Depto


# admin.site.register(Depto)
@admin.register(Depto)
class DeptosAdmin(admin.ModelAdmin):
    '''Clase Administracion del modelo Profile'''
    # la lista la muestra con los datos que solicito a continuacion
    list_display = ('pk', 'Depto','Fecha_visita', 'Numero_Contacto', 'Precio', 'Ambientes', 'Baños' )
    # de la lista la muestra los datos que linkean al ABM
    list_display_links = ('pk', 'Depto')
    # la lista la muestra con los datos que permite edicion en la misma lista a continuacion
    list_editable = ( 'Numero_Contacto', 'Fecha_visita','Ambientes', 'Baños', 'Precio')
    # muestra la opcion de busqueda y defino sobre que campos puedo buscar
    search_fields = (
        'Depto',
        'Ambientes',
        'Baños',
        'Precio',
        'Numero_Contacto',
        'Fecha_visita',
    )
    # muestra filtros para la lista
    list_filter = (
        'Fecha_visita',
        'Creado',
        'Modificado'
    )
