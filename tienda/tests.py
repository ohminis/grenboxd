from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Consulta
from django.urls import reverse

class QAIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@test.com', password='password123')

    # 1. Autenticación y Registro
    def test_auth_01_registro_exitoso(self):
        response = self.client.post(reverse('registro'), {
            'username': 'newuser',
            'email': 'new@test.com',
            'password': 'newpassword123'
        })
        # If it redirects to inicio or creates user
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_auth_02_ingreso_exitoso(self):
        response = self.client.post(reverse('ingreso'), {
            'username': 'testuser',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 302) # Redirects to inicio

    def test_auth_03_ingreso_fallido(self):
        response = self.client.post(reverse('ingreso'), {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200) # Re-renders form with errors

    def test_auth_04_cierre_sesion(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('salir'))
        self.assertEqual(response.status_code, 302) # Redirects to inicio

    # 2. Gestión de Usuarios
    def test_crud_01_acceso_denegado(self):
        response = self.client.get(reverse('lista_usuarios'))
        self.assertEqual(response.status_code, 302) # Redirect to login

    def test_crud_02_acceso_permitido(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('lista_usuarios'))
        self.assertEqual(response.status_code, 200)

    def test_crud_03_editar_usuario(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('editar_usuario', args=[self.user.id]), {
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'updated@test.com'
        })
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, 'updated@test.com')

    def test_crud_04_eliminar_usuario(self):
        self.client.login(username='testuser', password='password123')
        user2 = User.objects.create_user(username='delete_me', password='123')
        response = self.client.post(reverse('eliminar_usuario', args=[user2.id]))
        self.assertFalse(User.objects.filter(username='delete_me').exists())

    # 3. API
    def test_api_01_carga(self):
        response = self.client.get(reverse('inicio'))
        self.assertEqual(response.status_code, 200)

    # 4. Carrito
    def test_cart_01_agregar(self):
        response = self.client.post(reverse('agregar_al_carrito', args=[1]), {
            'cantidad': 1, 'nombre': 'Manzana', 'precio': 100.0, 'imagen': 'url'
        })
        self.assertEqual(self.client.session.get('carrito', {}).get('1', {}).get('cantidad'), 1)

    def test_cart_02_sumar_cantidades(self):
        self.client.post(reverse('agregar_al_carrito', args=[1]), {
            'cantidad': 1, 'nombre': 'Manzana', 'precio': 100.0, 'imagen': 'url'
        })
        self.client.post(reverse('agregar_al_carrito', args=[1]), {
            'cantidad': 2, 'nombre': 'Manzana', 'precio': 100.0, 'imagen': 'url'
        })
        self.assertEqual(self.client.session.get('carrito', {}).get('1', {}).get('cantidad'), 3)

    def test_cart_03_total(self):
        self.client.post(reverse('agregar_al_carrito', args=[1]), {
            'cantidad': 2, 'nombre': 'Manzana', 'precio': 100.0, 'imagen': 'url'
        })
        response = self.client.get(reverse('ver_carrito'))
        self.assertEqual(response.status_code, 200)

    def test_cart_04_limpiar(self):
        self.client.post(reverse('agregar_al_carrito', args=[1]), {
            'cantidad': 1, 'nombre': 'Manzana', 'precio': 100.0, 'imagen': 'url'
        })
        self.client.get(reverse('limpiar_carrito'))
        self.assertNotIn('carrito', self.client.session)

    # 5. Formulario
    def test_form_01_enviar(self):
        response = self.client.post(reverse('consulta'), {
            'nombre': 'Omar', 'email': 'omar@omar.com', 'mensaje': 'Hola'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Consulta.objects.filter(nombre='Omar').exists())
