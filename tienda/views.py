import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, ConsultaForm
from .models import Consulta

# ==========================================
# 3. CONECTAR CON API Y CONFIGURAR STOCK
# ==========================================
def inicio(request):
    productos = []
    try:
        response = requests.get('https://fakestoreapi.com/products/category/electronics', timeout=5)
        if response.status_code == 200:
            api_productos = response.json()
            
            nombres_verduleria = [
                "Cajón de Tomates", 
                "Papas Seleccionadas", 
                "Bananas Ecuador", 
                "Manzanas Rojas", 
                "Lechuga Capuchina", 
                "Zanahorias Asadas"
            ]
            
            # URLs estables de Pixabay / Unsplash Source optimizadas
            imagenes_verduleria = [
                "https://cdn.pixabay.com/photo/2011/03/16/16/01/tomatoes-5356_250.jpg",
                "https://cdn.pixabay.com/photo/2014/08/06/20/32/potatoes-411975_250.jpg",
                "https://cdn.pixabay.com/photo/2016/01/03/05/20/bananas-1119047_250.jpg",
                "https://cdn.pixabay.com/photo/2016/08/12/22/34/apple-1589874_250.jpg",
                "https://cdn.pixabay.com/photo/2016/03/05/19/14/salad-1238318_250.jpg",
                "https://cdn.pixabay.com/photo/2016/08/03/17/29/carrots-1567195_250.jpg"
            ]
            
            for i, prod in enumerate(api_productos):
                if i < len(nombres_verduleria):
                    # Multiplicamos el precio original por 100 para simular precios en pesos argentinos reales
                    precio_arg = round(float(prod['price']) * 100, 2)
                    
                    productos.append({
                        'id': prod['id'],
                        'title': nombres_verduleria[i],
                        'image': imagenes_verduleria[i],
                        'price': precio_arg
                    })
    except Exception:
        pass

    return render(request, 'tienda/inicio.html', {'productos': productos})

# ==========================================
# LÓGICA DEL CARRITO DE COMPRAS (SESIONES)
# ==========================================
def agregar_al_carrito(request, producto_id):
    # Obtener la cantidad enviada desde el formulario, por defecto 1
    cantidad = int(request.POST.get('cantidad', 1))
    nombre = request.POST.get('nombre')
    precio = float(request.POST.get('precio'))
    imagen = request.POST.get('imagen')

    # Inicializar el carrito en la sesión si no existe
    if 'carrito' not in request.session:
        request.session['carrito'] = {}
    
    carrito = request.session['carrito']
    id_str = str(producto_id)

    if id_str in carrito:
        carrito[id_str]['cantidad'] += cantidad
        carrito[id_str]['subtotal'] = carrito[id_str]['cantidad'] * carrito[id_str]['precio']
    else:
        carrito[id_str] = {
            'producto_id': producto_id,
            'nombre': nombre,
            'precio': precio,
            'imagen': imagen,
            'cantidad': cantidad,
            'subtotal': cantidad * precio
        }
    
    request.session.modified = True
    return redirect('ver_carrito')

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    total = sum(item['subtotal'] for item in carrito.values())
    return render(request, 'tienda/carrito.html', {'carrito': carrito, 'total': total})

def limpiar_carrito(request):
    if 'carrito' in request.session:
        del request.session['carrito']
    return redirect('inicio')


def nosotros(request):
    return render(request, 'tienda/nosotros.html')

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('inicio')
    else:
        form = RegistroForm()
    return render(request, 'tienda/registro.html', {'form': form})

def ingreso_usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'tienda/ingreso.html', {'form': form})

def salir_usuario(request):
    logout(request)
    return redirect('inicio')

def crear_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'tienda/consulta_exitosa.html')
    else:
        form = ConsultaForm()
    return render(request, 'tienda/consulta.html', {'form': form})

@login_required
def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'tienda/usuarios_list.html', {'usuarios': usuarios})

@login_required
def editar_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        usuario.first_name = request.POST.get('first_name')
        usuario.last_name = request.POST.get('last_name')
        usuario.email = request.POST.get('email')
        usuario.save()
        return redirect('lista_usuarios')
    return render(request, 'tienda/usuarios_edit.html', {'usuario': usuario})

@login_required
def eliminar_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')
    return render(request, 'tienda/usuarios_delete.html', {'usuario': usuario})



