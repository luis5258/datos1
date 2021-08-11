# <!-- {% extends 'index.html' %}

# {% block content %}

# <p></p>
# <h1 class="center">REGISTROS DE SURTIDOS INGRESADOS</h1>

# <p></p>
# <h4>Status: (Activo = 1, Baja = 2)</h4>
# <a class="btn btn-success col-2" href="{% url 'activop' %}">Activo</a>
# <a class="btn btn-danger col-2" href="{% url 'bajap' %}">Baja</a>

# <p></p>

# {% if mensaje %}
# <div class="alert alert-success" role="alert">
#     Se ha eliminado correctamente
# </div>
# {% endif %}


# <table class="table table-bordered table-dark">
#     <thead>
#       <tr>
#         <th scope="col">ID</th>
#         <th scope="col">Producto</th>
#         <th scope="col">Status</th>
#         <th scope="col">Fecha</th>
#         <th scope="col">¿Producto apto?</th>
#       </tr>
#     </thead>
#     <tbody>
      
#         {% for Producto in productos %}
#         <tr>
#             <th scope="row">{{ Producto.id }}</th>
#             <td>{{ Producto.producto }}</td>
#             <td>{{ Producto.tipoStatus  }}</td>
#             <td>{{ Producto.fecha }}</td>
#             <td>{{ Producto.apto }}</td>
         
            
            
#         </tr>  
#         {% endfor %}
       
#     </tbody>
#   </table>
# {% endblock %} -->
