from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Usuario(models.Model):
    nombre = models.CharField(max_length=150)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128) 
    codigo_unico = models.CharField(max_length=50, unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def set_password(self, raw_password):
        self.contraseña = make_password(raw_password) #encriptamiento de contraseña

    def check_password(self, raw_password):
        return check_password(raw_password, self.contraseña) #Aqui se verifica la contraseña encriptada

    def __str__(self):
        return self.nombre
