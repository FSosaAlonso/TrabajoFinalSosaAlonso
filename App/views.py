from itertools import product
from multiprocessing.sharedctypes import Value
from django.shortcuts import render, HttpResponse
from App.models import *
from App.forms import *

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):

    avatares = Avatar.objects.filter(user=request.user.id)

    return render(request, "App/inicio.html", {"url":avatares[0].imagen.url})

def aboutme(request):
        
    avatares = Avatar.objects.filter(user=request.user.id)
    
    return render(request, "App/Aboutme.html", {"url":avatares[0].imagen.url})



def empleados(request):
    
    avatares = Avatar.objects.filter(user=request.user.id)

    if request.method == 'POST':

        miFormulario = EmpleadosForm(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            info = miFormulario.cleaned_data
            print(info)

            empleado = Empleados(nombre=info['nombre'], apellido=info['apellido'], DNI=info['DNI'])
            empleado.save()

            return render(request, "App/inicio.html", {"url":avatares[0].imagen.url})
    else:
        miFormulario = EmpleadosForm()

    return render(request, "App/empleados.html", {"miFormulario":miFormulario, "url":avatares[0].imagen.url})

class EmpleadoList(LoginRequiredMixin, ListView):
    
    model = Empleados
    template_name = "App/empleado_list.html"
    
    def empleadolist(request):
        
        avatares = Avatar.objects.filter(user=request.user.id)
        
        return render(request, "App/empleado_list.html", {"url":avatares[0].imagen.url})



def proveedores(request):
    
    avatares = Avatar.objects.filter(user=request.user.id)

    if request.method == 'POST':

        miFormulario =ProveedoresForm(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            info = miFormulario.cleaned_data
            
            empleado = Proveedores(razonsocial=info['razonsocial'], productos=info['productos'], telefono=info['telefono'])
            empleado.save()

            return render(request, "App/inicio.html", {"url":avatares[0].imagen.url})
    else:
        miFormulario = ProveedoresForm()

    return render(request, "App/proveedores.html", {"miFormulario":miFormulario, "url":avatares[0].imagen.url})

class ProveedorList(LoginRequiredMixin, ListView):
    
    model = Proveedores
    template_name = "App/proveedor_list.html"
    
    def proveedorlist(request):
                
        return render(request, "App/proveedor_list.html")

class ProveedorDetalle(DetailView):
    
    model = Proveedores
    template_name = "App/proveedor_detalle.html"

class ProveedorCreacion(CreateView):
    
    model = Proveedores
    success_url = "/proveedor/list"
    fields = ['razonsocial', 'productos', 'telefono']

class ProveedorUpdate(UpdateView):
    
    model = Proveedores
    success_url = "/proveedor/list"
    fields = ['razonsocial', 'productos', 'telefono']

class ProveedorDelete(DeleteView):
    
    model = Proveedores
    success_url = "/proveedor/list"



def clientes(request):
    
    avatares = Avatar.objects.filter(user=request.user.id)

    if request.method == 'POST':

        miFormulario = ClientesForm(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            info = miFormulario.cleaned_data
            print(info)

            cliente = Clientes(nombre=info['nombre'], apellido=info['apellido'], fechafactura=info['fechafactura'],
            telefono=info['telefono'])
            cliente.save()

            return render(request, "App/inicio.html", {"url":avatares[0].imagen.url})
    else:
        miFormulario = ClientesForm()

    return render(request, "App/clientes.html", {"miFormulario":miFormulario, "url":avatares[0].imagen.url})

class ClienteList(LoginRequiredMixin, ListView):
    
    model = Clientes
    template_name = "App/clientes_list.html"
    
    def clientelist(request):
        
        return render(request, "App/clientes_list.html")



def buscar(request):
    
    avatares = Avatar.objects.filter(user=request.user.id)

    if request.GET['proveedores']:

        productos = request.GET['proveedores']

        proveedores = Proveedores.objects.filter(productos__icontains=productos)

        return render(request, "App/inicio.html", {"proveedores":proveedores,"productos":productos, "url":avatares[0].imagen.url})
       
    else:
        respuesta = "No se detecto ningún valor. Por favor ingrese datos para la busqueda de producto"

        return HttpResponse(respuesta)



def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contra)
            
            if user is not None:
               login(request, user)
                
               return render(request, "App/Inicio.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request,"App/Inicio.html", {"mensaje":"Error, datos incorrectos"})
        else:
            return render(request, "App/inicio.html", {"mensaje":"Error, formulario erroneo"})
    form = AuthenticationForm()
    return render(request, "App/login.html", {'form':form})

def register(request):
    
    if request.method == 'POST':
        
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            
            usermame = form.cleaned_data['username']
            form.save()
            return render(request,"App/inicio.html", {"mensaje": f"Usuario creado. Bienvenido {usermame}"})
    
    else:
        form = UserRegisterForm()
        
    return render(request, "App/registro.html", {"form":form})

def editarPerfil(request):
    
    usuario = request.user
    
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            
            info = miFormulario.cleaned_data
            
            usuario.email = info['email']
            usuario.password1 = info['password1']
            usuario.password2 = info['password2']
            usuario.save()
            
            return render(request, "App/inicio.html")
    else:
        
        miFormulario = UserEditForm(initial={'email':usuario.email})
    return render(request, "App/editarPerfil.html", {"miFormulario":miFormulario, "usuario": usuario})

