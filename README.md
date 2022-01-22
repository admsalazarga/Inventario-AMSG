# Inventario-AMSG

Prueba técnica: Esta API administra el inventario de bienes almacenados en la empresa AMSG. La API cuenta con los siguientes recursos:

* Stocks

## Pre-Requisitos 📋

Deberá contar con los siguientes paquetes instalados:

* Python 3.9.4 https://www.python.org/downloads/
* Django 4.0.1 https://www.djangoproject.com/download/ 
* Django Rest Framework 3.13.1 https://www.django-rest-framework.org/

Se recomienda el uso de la última versión de revisión de cada serie Python y Django.




### Instalación 🔧

Asegúrese de tener instalado virtualenv globalmente, o ejecute:

```
$ pip install virtualenv
```

Obtenga este repositorio en su PC

```
$ git clone https://github.com/admsalazarga/Inventario-AMSG.git
 ```

*Dependencias

Diríjase con _cd_ al repositorio anterior 
```
$ cd Inventario-AMSG
```
Cree y encienda su entorno virtual:
```
$ virtualenv  venv -p python
$ source venv/bin/activate
pip install django
pip install djangorestframework
```
 
Instale las dependencias necesarias para ejecutar la aplicación:
```
$ pip install -r requirements.txt
```
Haz que esas migraciones funcionen
```
$ python manage.py makemigrations
$ python manage.py migrate
```
Escribir usuario y contraseña
```
$ python manage.py createsuperuser
```


## Ejecución ⚙️

Encienda el servidor:

```
$ python manage.py runserver

```
Ahora puede acceder al servicio de archivo api en su navegador usando

```
http://localhost:8000/admin
http://localhost:8000/stocks

```


## Usuarios de prueba 🤓

Administrador

* usuario: admin
* contraseña: 12345


## Autores ✒️

* **Adriana Marcela Salazar**




---
