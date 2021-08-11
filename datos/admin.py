from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.



class registroAdmin(admin.ModelAdmin): #Para dar un diseño mas ordenado en la pantalla de datos
    list_display = ("corral","cliente", "producto", "cantidad", "fecha", "estado")
    # autocomplete_fields=["corral", 'producto']

class corralAdmin(admin.ModelAdmin):
    # search_fields = ("corral"),
    list_display = ("corral", "cliente", "tipoStatus", "fecha")
    

class productoAdmin(admin.ModelAdmin): 
    # search_fields = ("producto"),
    list_display = ("producto", "tipoStatus", "fecha", "apto")
    

class clienteAdmin(admin.ModelAdmin): 
    list_display = ("nombre", "direccion", "ciudad", "rfc","email","contacto","numero")
    

class provedorAdmin(admin.ModelAdmin): 
    list_display = ("nombre", "direccion", "ciudad", "rfc","email","contacto","numero")
    

class operadorAdmin(admin.ModelAdmin): 
    list_display = ("nombre", "estado")

class tipo_animalAdmin(admin.ModelAdmin): 
    list_display = ("descripcion", "estado")


class materia_primaAdmin(admin.ModelAdmin): 
    list_display = ("descripcion", "precio_unitario", "unidad", "estado")

class contenedores_mat_primaAdmin(admin.ModelAdmin): 
    list_display = ("clave", "cliente", "capacidad", "estado")

class contenedores_productoAdmin(admin.ModelAdmin): 
    list_display = ("claves", "provedor", "capacidad", "estado")

class estadoAdmin(admin.ModelAdmin): 
    list_display = ("estado",)


class surtibleAdmin(admin.ModelAdmin): 
    list_display = ("apto",)

class unidadAdmin(admin.ModelAdmin): 
    list_display = ("unidad",)

class corra_clienteAdmin(admin.ModelAdmin): 
    list_display = ("cliente",)

admin.site.register(registro, registroAdmin)
admin.site.register(Corral, corralAdmin)
admin.site.register(Producto, productoAdmin)
admin.site.register(Cliente, clienteAdmin)
admin.site.register(Provedor, provedorAdmin)
admin.site.register(Operador, operadorAdmin)
admin.site.register(Materia_prima, materia_primaAdmin)
admin.site.register(Contenedores_Mat_prima, contenedores_mat_primaAdmin)
admin.site.register(Contenedores_Producto, contenedores_productoAdmin)

admin.site.register(status, estadoAdmin)
admin.site.register(surtible, surtibleAdmin)
admin.site.register(Unidad, unidadAdmin)
admin.site.register(Cliente_corral, corra_clienteAdmin)

