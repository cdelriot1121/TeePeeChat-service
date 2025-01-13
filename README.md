# 🚀 **TeePeeChat Service - Backend en Django**

¡Bienvenidos al backend de **TeePeeChat**, una aplicación de mensajería en tiempo real! Este repositorio contiene el servicio web de la aplicación, desarrollado con el framework **Django** y preparado para interactuar con el frontend en React. 

El propósito de este proyecto es proporcionar la lógica del servidor para el envío y recepción de mensajes en tiempo real, autenticación de usuarios y demás funcionalidades necesarias para el funcionamiento de la app de mensajería.

<div align="center">
  <img width="180" height="180" src="https://img.icons8.com/fluency/100/chat--v3.png" alt="chat--v3"/>
</div>

## 🛠️ **Tecnologías utilizadas**

- **Django**: Framework web para Python, utilizado para crear aplicaciones web rápidas y seguras.
- **Django Channels**: Para manejar la mensajería en tiempo real usando WebSockets.
- **Python**: Lenguaje de programación usado para el desarrollo del backend.
- **SQLite/PostgreSQL**: Base de datos (configurable) para almacenar los datos de la aplicación.

## 🔧 **Instalación y Configuración**

Sigue los siguientes pasos para configurar el entorno de desarrollo y comenzar a contribuir al proyecto:

### 1. Clonar el repositorio

Primero, clona este repositorio a tu máquina local:

```bash
git clone https://github.com/cdelriot1121/TeePeeChat-service
```
```
cd TeePeeChat-Service
```

### 2. Crear un entorno virtual

Es recomendable usar un entorno virtual para instalar las dependencias, si ya tienes tu entorno virtual revisa tener los requerimientos del archivo txt. Para ello, puedes usar el siguiente comando:

**Si usas `venv`**:

```bash
python -m venv env-for-teepeechat
```

**Activar el entorno virtual**:

- En **Windows**:

```bash
env-for-teepeechat\Scripts\activate
```

- En **Mac/Linux**:

```bash
source env-for-teepeechat/bin/activate
```

### 3. Instalar las dependencias

Asegúrate de que el entorno virtual esté activado y luego instala las dependencias del proyecto desde el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Configuración del proyecto

Asegúrate tambien de que todos los archivos necesarios para la base de datos y otros componentes estén configurados adecuadamente. Si es la primera vez que inicias el proyecto, realiza las migraciones para configurar la base de datos:

(este puede ser opcional XD)
```bash
python manage.py makemigrations 
```
**Ejecute el comando migrate**

```bash
python manage.py migrate
```

### 5. Ejecutar el servidor de desarrollo

Una vez todo este ya configurado, puedes ejecutar el servidor de desarrollo de Django:

```bash
python manage.py runserver
```

Esto iniciará el servidor localmente en `http://127.0.0.1:8000/`.

### 6. Contribuir

Si deseas contribuir al proyecto, asegúrate de seguir estos pasos antes de enviar un PR:

- Realiza los cambios en una nueva rama, de tu fork
- Asegúrate de que el código sea compatible con el formato PEP8 (importante).
- Ejecuta las pruebas para asegurar que el código no rompa nada (Puedes buscar en la documentación de django para hacer test a unidades y modelos).

Para ejecutar las pruebas de Django:

```bash
python manage.py test
```

## 🌐 **Frontend - React**

Este repositorio contiene el backend de la aplicación de mensajería. Si deseas ver el frontend desarrollado en React, puedes encontrar el repositorio correspondiente aquí:

[TeePeeChat Frontend (React)](https://github.com/cdelriot1121/TeePeeChat-Template)