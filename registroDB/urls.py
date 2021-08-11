
from datos.views import *
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',loginView.register, name='registro'),
    
    path('inicio/', indexView.inicios, name = "inicio"),
    path('Contenido/', indexView.formulario, name = "formulario"),


 
    path('register/', loginView.register, name='registro'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
	path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),


    path('registroindex', formularioView.index, name = "registarDatos"),
    path('producto/', formularioView.Producto, name = "productodate"),
    path('corral/', formularioView.Corral, name = "corraldate"),
    path('Clientes/', formularioView.Cliente, name = "clientedate"),
    path('Provedores/', formularioView.Provedor, name = "provedordate"),
    path('Operadores/', formularioView.Operador, name = "operadordate"),
    path('Materia_prima/', formularioView.Materia_prima, name = "materiaaprimadate"),
    path('Tipo_animal/', formularioView.Tipo_animal, name = "tipoanimaldate"),
    path('Contenedores_Materia_Prima/', formularioView.Contenedores_mat_prima, name = "contenedoresMPdate"),
    path('Contenedores_Productos/', formularioView.Contenedores_producto, name = "contenedoresProducto"),

    path('guardado/', guardarView.procesar_formulario, name="guardarRegistro"),
    path('guardado_registro_corral/', guardarView.procesar_corral, name="guardarCorral"),
    path('guardado_registro_producto/', guardarView.procesar_producto, name="guardarProducto"),
    path('guardado_registro_cliente/', guardarView.procesar_cliente, name="guardarCliente"),
    path('guardado_registro_provedor/', guardarView.procesar_provedor, name="guardarProvedor"),
    path('guardado_registro_operador/', guardarView.procesar_operador, name="guardarOperador"),
    path('guardado_registro_materia_prima/', guardarView.procesar_materia_prima, name="guardarMateriaPrima"),
    path('guardado_registro_tipo_animal/', guardarView.procesar_tipo_animal, name="guardarTipoAnimal"),
    path('guardado_registro_contenedores_materia_prima/', guardarView.procesar_contenedores_materia_prima, name="guardarContenedorsMP"),
    path('guardado_registro_contenedores_producto/', guardarView.procesar_contenedor_producto, name="guardarContenedorsProducto"),

    path('tabla_de_registro/', tablaView.lista,  name = "lista"),
    path('tabla_de_corrales/', tablaView.tabla_corral,  name = "corrales"),
    path('tabla_de_productos/', tablaView.tabla_productos,  name = "productos"),
    path('tabla_de_cliente/', tablaView.tabla_cliente,  name = "clientes"),
    path('tabla_de_provedores/', tablaView.tabla_provedor,  name = "provedores"),
    # path('tabla_de_operadores/', tablaView.tabla_operador,  name = "operadores"),

  
    path('editar/<int:id_registros>', editarYactualizarView.edit, name ="editar"),
    path('actualizarRegistro/<int:id_registros>', editarYactualizarView.actualizar, name ='actualizar'),
    path('editarCorrales/<int:id_Corrals>', editarYactualizarView.editCorral, name ="editarCorral"),
    path('actualizarCorrales/<int:id_Corrals>', editarYactualizarView.actualizarCorral, name ='actualizarCorral'),
    


    path('eliminarRegistro/<id>', eliminarView.deleteRegistro, name ='eliminarRegistro'),
    path('eliminarCorral/<id>', eliminarView.delete, name ='eliminar'),


    path('estado/', filtrosView.tabla_status, name = "status"),
    path('surtible/', filtrosView.tabla_apto, name = "apto"),
  
    path('Reporte_Registro/', reporteView.reporte_registro, name = "reporteRegistro"),
    path('Reporte_Registro_USUARIO_<int:id_Cliente>/', reporteView.editCliente, name ="reporteCliente"),
#     path('Reporte_Registro_USUARIO_1/', reporteView.reporte_registro1),
#     path('Reporte_Registro_USUARIO_2/', reporteView.reporte_registro2),
#     path('Reporte_Registro_USUARIO_3/', reporteView.reporte_registro3),
#     path('Reporte_Registro_USUARIO_4/', reporteView.reporte_registro4),
#     path('Reporte_Registro_USUARIO_5/', reporteView.reporte_registro5),
#     path('Reporte_Registro_USUARIO_6/', reporteView.reporte_registro6),
#     path('Reporte_Registro_USUARIO_7/', reporteView.reporte_registro7),
#     path('Reporte_Registro_USUARIO_8/', reporteView.reporte_registro8),
#     path('Reporte_Registro_USUARIO_9/', reporteView.reporte_registro9),
#     path('Reporte_Registro_USUARIO_10/', reporteView.reporte_registro10),
]


