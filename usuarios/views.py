from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Usuario

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            correo = data.get('correo')
            contraseña = data.get('contraseña')

            if not correo or not contraseña:
                return JsonResponse({'message': 'Correo y contraseña son requeridos', 'status': 'error'}, status=400)

            try:
                usuario = Usuario.objects.get(correo=correo)
                if usuario.check_password(contraseña):
                    return JsonResponse({'message': 'Login exitoso', 'status': 'success'}, status=200)
                else:
                    return JsonResponse({'message': 'Contraseña incorrecta', 'status': 'error'}, status=401)
            except Usuario.DoesNotExist:
                return JsonResponse({'message': 'Usuario no encontrado', 'status': 'error'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'JSON inválido', 'status': 'error'}, status=400)

    return JsonResponse({'message': 'Método no permitido', 'status': 'error'}, status=405)

@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nombre = data.get('nombre')
            correo = data.get('correo')
            contraseña = data.get('contraseña')

            # Validar que todos los campos estén presentes
            if not nombre or not correo or not contraseña:
                return JsonResponse({'message': 'Nombre, correo y contraseña son requeridos', 'status': 'error'}, status=400)

            # Verificar si el correo ya está registrado
            if Usuario.objects.filter(correo=correo).exists():
                return JsonResponse({'message': 'Correo ya registrado', 'status': 'error'}, status=400)

            # Crear y guardar el nuevo usuario
            usuario = Usuario(
                nombre=nombre,
                correo=correo,
                codigo_unico=f"USR-{correo.split('@')[0]}",
            )
            usuario.set_password(contraseña)
            usuario.save()

            return JsonResponse({'message': 'Registro exitoso', 'status': 'success'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'JSON inválido', 'status': 'error'}, status=400)

    return JsonResponse({'message': 'Método no permitido', 'status': 'error'}, status=405)
