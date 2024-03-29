# Projecto API Server

## Objetivo: programar un API Server utilizando Django. Django es un framework escrito en Python para desarrollar aplicaciones web

## API endpoints

### 1- api/v1/devices

Descripción: retorna los dispositvos almacenados en la DB  
Métodos:
GET  

### 2- api/v1/{device}/interfaces

Descripción: agrega, elimina, modifica y retorna las interfaces de un {dispositivo} almacenaodo en la DB  

Métodos:  
GET  
POST  
&nbsp;&nbsp;Body:  
&nbsp;&nbsp;{  
&nbsp;&nbsp;&nbsp;&nbsp;"type": "Giga" o "Fast",  
&nbsp;&nbsp;&nbsp;&nbsp;"slot": 0 o 9,  
&nbsp;&nbsp;&nbsp;&nbsp;"port": 0 o 1,  
&nbsp;&nbsp;&nbsp;&nbsp;"ipv4_address": "X.X.X.X" o "none",  
&nbsp;&nbsp;&nbsp;&nbsp;"status": "u" o "d"  
&nbsp;&nbsp;}  
PATCH
&nbsp;&nbsp;Body:  
&nbsp;&nbsp;{  
&nbsp;&nbsp;&nbsp;&nbsp;"type": "Giga" o "Fast",  
&nbsp;&nbsp;&nbsp;&nbsp;"slot": 0 o 9,  
&nbsp;&nbsp;&nbsp;&nbsp;"port": 0 o 1,  
&nbsp;&nbsp;&nbsp;&nbsp;"ipv4_address": "X.X.X.X" o "none",  
&nbsp;&nbsp;&nbsp;&nbsp;"status": "u" o "d"  
&nbsp;&nbsp;}  
DELETE
&nbsp;&nbsp;Body:  
&nbsp;&nbsp;{  
&nbsp;&nbsp;&nbsp;&nbsp;"type": "Giga" o "Fast",  
&nbsp;&nbsp;&nbsp;&nbsp;"slot": 0 o 9,  
&nbsp;&nbsp;&nbsp;&nbsp;"port": 0 o 1,  
&nbsp;&nbsp;}  

### 3- api/v1/{device}/interfaces/{status}

Descripción: retorna las interfaces de un {dispositivo} almecenado en la DB según su estado {Up o Down}  

Métodos:  
GET  

### 4- api/v1/apitest

Descripción: verifica el funcionamiento del API, retornando todos los parametros del request enviados al API Server  

Métodos:
GET

## Base de datos

SQLite  

## Tablas DB

Devices  
Interfaces  
Usuarios  
Tokens  

## Adicionales: Production Server

Guia para configurar un servidor de producción que reemplace al servidor de desarrollo (Django)

[Config files](https://github.com/OctupusCloud/ApiServer/tree/main/Adicionales)

### Gunicorn Socket

/etc/system/systemd/gunicorn.socket

Configuración file Socket Nginx to Gunicorn

### Gunicorn HTTP WSGI Server

/etc/system/systemd/gunicorn.service

Configuración file Gunicorn Service

### Nginx Web Server

/etc/nginx/sites-enabled/nginx.conf (puede ser renombrado)

Configuración file Nginx

### Configuración Nginx y Gunicorn example

<https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04-es>

### Ed Scrimaglia, Año 2022
