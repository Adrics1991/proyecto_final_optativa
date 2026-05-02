# proyecto_final_optativa

## Objetivo
Aplicación base propuesta: chatbot en Python con Tkinter
Este proyecto consiste en un chatbot desarrollado en Python con Tkinter y una base de datos en formato JSON.
La aplicación permite realizar preguntas sobre plantas mediterráneas y obtener respuestas almacenadas en la base de datos.
El proyecto está versionado con GitHub, contenerizado con Docker y orquestado con Docker Compose.
## Instalación y ejecución
### 1. Clonar el repositorio
git clone https://github.com/usuario/chatbot-dam.git
cd chatbot-dam

### 2. Construir la imagen
docker build -t chatbot .

### 3. Levantar los servicios
docker compose up

### 4. Acceder a la aplicación
La aplicación queda disponible en el puerto 5000 del host:
http://localhost:5000

## Dockerfile
El Dockerfile utiliza la imagen base `python:3.11-slim`, instala dependencias y copia el código al contenedor.  
Al iniciar, ejecuta `main.py`.

## docker-compose.yml
Define el servicio `chatbot`, monta un volumen para persistir `base_datos.json` y expone el puerto 5000.

El archivo docker-compose.yml define el servicio principal del chatbot.
Se monta un volumen para persistir el archivo base_datos.json y se expone el puerto 5000, permitiendo acceder a la aplicación desde el host.
El servicio se construye a partir del Dockerfile y ejecuta automáticamente main.py.

## Problemas comunes

### ❗ Conflicto de puertos
Si el puerto 5000 está ocupado:
docker compose down
Modificar en docker-compose.yml:
  ports:
    - "5001:5000"

### ❗ Permisos en el volumen
Si el JSON no se actualiza:
chmod 666 data/base_datos.json
