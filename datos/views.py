
from django.contrib import messages
from datos.forms import cliente_corral, contenedores_mat_prima, contenedores_producto, formulario, corral, materia_prima, operador, producto, UserRegisterForm, provedor, tipo_animal
from datos.models import Cliente_corral, Contenedores_Mat_prima, Contenedores_Producto, Corral, Materia_prima, Producto, Provedor, Tipo_animal, registro, Cliente,status, surtible, Operador
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from datos.forms import registro, corral, producto,cliente




class indexView(HttpRequest):

    def inicios(request):
        return render(request, "base/inicio.html")

    def formulario(request):
        return render(request, "base/formulario.html")




class loginView(HttpRequest):

    def register(request):
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                messages.success(request, f'Usuario "{username}" creado')
                return redirect('login')
        else:
            form = UserRegisterForm()
        context = { 'form' : form }
        return render(request, 'registro.html', context)




class formularioView(HttpRequest):
    
    def index(request):
        registro1 = formulario()
        Corrals = Corral.objects.filter(tipoStatus = "Activo")
        productos = Producto.objects.filter(apto = "Si")
        Clientes = Cliente.objects.all()
        registros = registro.objects.all()
        return render(request, "formulario/registroindex.html", {'form': registro1,"Corrals":Corrals, 
        "productos":productos, "Clientes":Clientes, "registros":registros})

    def Corral(request):
        Clientes = Cliente.objects.all()
        statu = status.objects.all()
        Cliente1_corral = cliente_corral()
        Clientes_corral = Cliente_corral.objects.all()
        Corrals = Corral.objects.all()     
        return render(request, "formulario/corralIndex.html", {"Clientes":Clientes, "statu":statu, 
        "form8":Cliente1_corral,"Clientes_corral": Clientes_corral, "Corrals":Corrals })
    
    def Producto(request):
        Producto1 = producto()
        statu = status.objects.all()
        surtibles = surtible.objects.all()
        productos = Producto.objects.all()
        return render(request, "formulario/productoIndex.html", {'form3': Producto1, "statu":statu, "surtibles":surtibles,
        "productos":productos})

    def Cliente(request):
        Cliente1 = cliente()
        Clientes = Cliente.objects.all()
        return render(request, "formulario/clienteindex.html", {'form4': Cliente1, "Clientes":Clientes})
    
    def Provedor(request):
        Provedor1 = provedor()
        Provedores = Provedor.objects.all()
        return render(request, "formulario/provedorindex.html", {'form5': Provedor1, "Provedores":Provedores})
    
    def Operador(request):
        Operadora = operador()
        Operadores = Operador.objects.all()
        return render(request, "mixto/tablaOperador.html", {'form6': Operadora, "Operadores":Operadores})

    def Materia_prima(request):
        Material_prima = materia_prima()
        Materias_prima = Materia_prima.objects.all() 
        return render(request, "mixto/materiaPrimaindex.html", {'form7': Material_prima, "Materias_prima":Materias_prima})

    def Tipo_animal(request):
        Tipo_animal1 = tipo_animal()
        Tipos_animal = Tipo_animal.objects.all()
        return render(request, "mixto/tipoAnimalindex.html", {'form8': Tipo_animal1, "Tipos_animal":Tipos_animal})    

    def Contenedores_mat_prima(request):
        Contenedores_mat_prima1 = contenedores_mat_prima()
        Contenedores_Mat_primas = Contenedores_Mat_prima.objects.all()
        return render(request, "mixto/contenedoresMatPrimaindex.html", {'form9': Contenedores_mat_prima1, "Contenedores_Mat_primas":Contenedores_Mat_primas})

    def Contenedores_producto(request):
        Contenedores_producto1 = contenedores_producto()
        Contenedores_productos = Contenedores_Producto.objects.all()
        return render(request, "mixto/contenedoresProductoindex.html", {'form10': Contenedores_producto1, "Contenedores_productos":Contenedores_productos})

class guardarView(HttpRequest):
   
    def procesar_formulario(request):
        registro=formulario(request.POST)
        if registro.is_valid():
            registro.save()
            registro = formulario()
        return render(request, "formulario/registroindex.html", {"form":registro, "mensaje": 'ok'})

    def procesar_corral(request):
        Corral=corral(request.POST)
        if Corral.is_valid():
            Corral.save()
            Corral = corral()

        Cliente_corral = cliente_corral(request.POST)
        if Cliente_corral.is_valid():
            Cliente_corral.save()
            Cliente_corral = cliente_corral()
        return render(request, "formulario/corralIndex.html", {"form2":Corral, "form8":Cliente_corral, "mensaje": 'ok'})

    def procesar_producto(request):
        Producto = producto(request.POST)
        if Producto.is_valid():
            Producto.save()
            Producto = producto()
        return render(request, "formulario/productoIndex.html", {"form3":Producto, "mensaje": 'ok'})

    def procesar_cliente(request):
        Cliente=cliente(request.POST)
        if Cliente.is_valid():
            Cliente.save()
            Cliente = cliente()
        return render(request, "formulario/clienteindex.html", {"form4":Cliente, "mensaje": 'ok'})

    def procesar_provedor(request):
        Provedor = provedor(request.POST)
        if Provedor.is_valid():
            Provedor.save()
            Provedor = provedor()
        return render(request, "formulario/provedorindex.html", {"form5":Provedor, "mensaje": 'ok'})
    
    def procesar_operador(request):
        Operadora = operador(request.POST)
        if Operadora.is_valid():
            Operadora.save()
            Operadora = operador()
        return render(request, "mixto/tablaOperador.html", {"form5":Operadora, "mensaje": 'ok'})

    def procesar_materia_prima(request):
        Materia_prima = materia_prima(request.POST)
        if Materia_prima.is_valid():
            Materia_prima.save()
            Materia_prima = materia_prima()
        return render(request, "mixto/materiaPrimaindex.html", {"form7":Materia_prima, "mensaje": 'ok'})

    def procesar_tipo_animal(request):
        Tipo_animal = tipo_animal(request.POST)
        if Tipo_animal.is_valid():
            Tipo_animal.save()
            Tipo_animal = tipo_animal()
        return render(request, "mixto/tipoAnimalindex.html", {"form8":Tipo_animal, "mensaje": 'ok'})

    def procesar_contenedores_materia_prima(request):
        Contenedores_mat_prima = contenedores_mat_prima(request.POST)
        if Contenedores_mat_prima.is_valid():
            Contenedores_mat_prima.save()
            Contenedores_mat_prima = contenedores_mat_prima()
        return render(request, "mixto/contenedoresMatPrimaindex.html", {"form9":Contenedores_mat_prima, "mensaje": 'ok'})

    def procesar_contenedor_producto(request):
        Contenedores_producto = contenedores_producto(request.POST)
        if Contenedores_producto.is_valid():
            Contenedores_producto.save()
            Contenedores_producto = contenedores_producto()

        return render(request, "mixto/contenedoresProductoindex.html", {"form10":Contenedores_producto, "mensaje": 'ok'})



class tablaView(HttpRequest):

    def lista(request):
        registros = registro.objects.all()
        Corrals = Corral.objects.all()
        return render(request, "tablas/listas.html", {"registros":registros, "Corrals":Corrals})
    
    def tabla_corral(request):
        Corrals = Corral.objects.all()
        return render(request, "tablas/tablaCorral.html", {"Corrals":Corrals})

    def tabla_productos(request):
        productos = Producto.objects.all()
        return render(request, "tablas/tablaProductos.html", {"productos":productos})
    
    def tabla_cliente(request):
        Clientes = Cliente.objects.all()
        return render(request, "tablas/tablaClientes.html", {"Clientes":Clientes})   

    def tabla_provedor(request):
        Provedores = Provedor.objects.all()
        return render(request, "tablas/tablaProvedores.html", {"Provedores":Provedores}) 
    
    def tabla_operador(request):
        Operadores = Operador.objects.all()
        return render(request, "mixto/tablaOperador.html", {"Operadores":Operadores})





class editarYactualizarView(HttpRequest):

    def edit(request, id_registros):      
        registros = registro.objects.filter(id=id_registros).first()
        form = formulario(instance=registros)
        return render(request, "editar/editartabla.html", {"form":form, "registros": registros})
    
    def actualizar(request, id_registros):  
        registros = registro.objects.get(pk=id_registros)
        form = formulario(request.POST, instance=registros)
        if form.is_valid():
            form.save()
        registros = registro.objects.all()
        return render(request, "tablas/listas.html", {"registros":registros})

    def editCorral(request, id_Corrals):      
        Corrals = Corral.objects.filter(id=id_Corrals).first()
        form = corral(instance=Corrals)
        return render(request, "editar/editarCorrales.html", {"form":form, "Corrals": Corrals})
    
    def actualizarCorral(request, id_Corrals):  
        Corrals = Corral.objects.get(pk=id_Corrals)
        form = corral(request.POST, instance=Corrals)
        if form.is_valid():
            form.save()
        Corrals = Corral.objects.all()
        return render(request, "tablas/tablaCorral.html", {"Corrals":Corrals})

 


class eliminarView(HttpRequest):

    def deleteRegistro(request, id):
        registros = get_object_or_404(registro, id=id)
        registros.delete()
        registros = registro.objects.all()
        return render(request, "tablas/listas.html", {"registros":registros, "mensaje": 'ok'})
    
    def delete(request, id):
        Corrals = get_object_or_404(Corral, id=id)
        Corrals.delete()
        Corrals = Corral.objects.all()
        return render(request, "tablas/tablaCorral.html", {"Corrals":Corrals, "mensaje": 'ok'})




class filtrosView(HttpRequest):

    def tabla_status(request):
        statu = status.objects.all()
        return render(request, "filtro/status.html", {"statu":statu})
    
    def tabla_apto(request):
        surtibles = surtible.objects.all()
        return render(request, "filtro/surtible.html", {"surtibles":surtibles})

    def pendiente_registro(request):
        registros = registro.objects.filter(estado = 2)
        return render(request, "tablas/listas.html", {"registros":registros})


    

class reporteView(HttpRequest):
    def editCliente(request, id_Cliente):      
        Clientes = Cliente.objects.filter(id=id_Cliente).first()
        registros = registro.objects.filter(cliente = id_Cliente)
        return render(request, "reporte/imprimirRegistro.html", {"registros":registros, "Clientes": Clientes})

    def reporte_registro(request):  
        registros = registro.objects.all()
        # Corrals = Corral.objects.filter(tipoStatus=1)
        return render(request, "reporte/imprimirRegistro.html", {"registros":registros})

    # def reporte_registro1(request):  
    #     registros = registro.objects.filter(cliente=1)
    #     # Corrals = Corral.objects.filter(tipoStatus=1)
    #     return render(request, "reporte/imprimirRegistro.html", {"registros":registros})
    




















