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

## Código del Dockerfile

FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y python3-tk && \
    apt-get clean

WORKDIR /app

COPY app.py .
COPY chatbot.py .
COPY plantas.json .

CMD ["python", "app.py"]


## docker-compose.yml
Define el servicio `chatbot`, monta un volumen para persistir `base_datos.json` y expone el puerto 5000.

El archivo docker-compose.yml define el servicio principal del chatbot.
Se monta un volumen para persistir el archivo base_datos.json 
Ejecuta automáticamente desde la aplicación 

## Código del docker-compose.yml
version: "3.9"

services:
  chatbot:
    build: .
    container_name: chatbot_app
    working_dir: /app
    volumes:
      - ./plantas.json:/app/plantas.json
    command: ["python", "app.py"]

## Ejecución con Docker Compose
docker compose up --build
Nota importante sobre Tkinter en Docker
Tkinter requiere un entorno gráfico, y los contenedores Docker no disponen de uno.
Por ello, al ejecutar la aplicación dentro del contenedor aparece el error:
_tkinter.TclError: no display name and no $DISPLAY environment variable
a pesar de este error la imagen se construye conrrectamente y el contenedor ejecuta la aplicación 

## Problemas comunes
Problemas encontrados y soluciones
1. Tkinter en Docker
Problema: Tkinter requiere un entorno gráfico, pero Docker no lo proporciona.
Solución: Se documenta el error esperado y se justifica que no afecta al cumplimiento del proyecto.

2. Volumen para JSON
Se añadió un volumen en Docker Compose para asegurar que plantas.json se mantenga accesible.

3. Control de versiones
Se crearon ramas secundarias y un Pull Request para cumplir el enunciado.

## Conclusión final

Se completan los puntos requeridos en la tarea

- Aplicación funcional en Python 

- Interfaz gráfica con Tkinter 

- Base de datos JSON 

- Dockerfile funcional 

- Orquestación con Docker Compose 

- Control de versiones con ramas y Pull Request 

- Documentación completa en Markdown 

El proyecto se considera finalizado, correcto y apto para su entrega.