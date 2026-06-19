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
            
            # URLs estables de Unsplash optimizadas y libres de bloqueos de hotlinking
            imagenes_verduleria = [
                "https://images.unsplash.com/photo-1592924357228-91a4daadcfea?q=80&w=600&auto=format&fit=crop",  # Tomates
                "https://images.unsplash.com/photo-1518977676601-b53f82aba655?q=80&w=600&auto=format&fit=crop",  # Papas
                "https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?q=80&w=600&auto=format&fit=crop",  # Bananas
                "https://images.unsplash.com/photo-1568702846914-96b305d2aaeb?q=80&w=600&auto=format&fit=crop",  # Manzanas
                "https://images.unsplash.com/photo-1556801712-76c8eb07bbc9?q=80&w=600&auto=format&fit=crop",  # Lechuga
                "https://images.unsplash.com/photo-1598170845058-32b9d6a5da37?q=80&w=600&auto=format&fit=crop"   # Zanahorias
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
    cantidad = int(request.POST.get('cantidad', 1))
    nombre = request.POST.get('nombre')
    precio = float(request.POST.get('precio'))
    imagen = request.POST.get('imagen')

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
