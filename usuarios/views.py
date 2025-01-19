from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Usuario

@csrf_exempt  # Esto es solo para pruebas locales. En producción, usa CSRF correctamente.
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        correo = data.get('correo')
        contraseña = data.get('contraseña')

        try:
            usuario = Usuario.objects.get(correo=correo)
            if usuario.check_password(contraseña):
                return JsonResponse({'message': 'Login exitoso', 'status': 'success'}, status=200)
            else:
                return JsonResponse({'message': 'Contraseña incorrecta', 'status': 'error'}, status=401)
        except Usuario.DoesNotExist:
            return JsonResponse({'message': 'Usuario no encontrado', 'status': 'error'}, status=404)
    return JsonResponse({'message': 'Método no permitido', 'status': 'error'}, status=405)

@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        nombre = data.get('nombre')
        correo = data.get('correo')
        contraseña = data.get('contraseña')

        if Usuario.objects.filter(correo=correo).exists():
            return JsonResponse({'message': 'Correo ya registrado', 'status': 'error'}, status=400)

        usuario = Usuario(
            nombre=nombre,
            correo=correo,
            codigo_unico=f"USR-{correo.split('@')[0]}",
        )
        usuario.set_password(contraseña)
        usuario.save()

        return JsonResponse({'message': 'Registro exitoso', 'status': 'success'}, status=201)

    return JsonResponse({'message': 'Método no permitido', 'status': 'error'}, status=405)
