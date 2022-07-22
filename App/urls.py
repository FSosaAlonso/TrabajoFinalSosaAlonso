from django.urls import path
from App import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('Empleados', views.empleados, name="Empleados"),
    path('Proveedores', views.proveedores, name="Proveedores"),
    path('Clientes', views.clientes, name="Clientes"),
    path('Aboutme', views.aboutme, name="Aboutme"),
    path('buscar/', views.buscar),
    
    path('proveedor/list', views.ProveedorList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.ProveedorDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.ProveedorCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.ProveedorUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.ProveedorDelete.as_view(), name='Delete'),

    path('cliente/list', views.ClienteList.as_view(), name='List'),
    path('empleado/list', views.EmpleadoList.as_view(), name='List'),
  
    path('login', views.login_request, name='Login'),
    path('register', views.register, name = 'Register'),
    path('logout', LogoutView.as_view(template_name= 'App/logout.html'), name = 'Logout'),
    
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
]