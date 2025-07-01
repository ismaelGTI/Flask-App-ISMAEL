# Flask App ISMAEL

¡Bienvenido a la aplicación Flask de José Ismael Marín Ghalem!

Este proyecto es una app web moderna y creativa hecha con Flask, lista para ejecutarse localmente, en contenedor Docker o desplegarse en cualquier plataforma compatible.

## Características

- Página de inicio con diseño moderno y tarjetas destacadas
- Página "Sobre mí" con animaciones, botón de copiar email y datos de contacto
- Formulario de contacto funcional con validación y mensajes flash
- Página sorpresa interactiva con datos curiosos y animaciones
- Estilos CSS personalizados y responsivos
- Preparada para despliegue en Docker y Docker Hub

## Estructura del proyecto

```
flask_app/
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
├── mensajes.txt
├── static/
│   └── estilos.css
└── templates/
    ├── about.html
    ├── contacto.html
    ├── index.html
    └── sorpresa.html
```

## Ejecución local

1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Ejecuta la app:
   ```bash
   python app.py
   ```
3. Abre tu navegador en [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Uso con Docker o Podman

1. Construye la imagen:
   ```bash
   docker build -t ismaelmrn/flask-app:latest .
   # o con podman
   podman build -t ismaelmrn/flask-app:latest .
   ```
2. Ejecuta el contenedor (puerto local 6000 → contenedor 5000): *Puede ser cualquier puerto local, 6000 es en mi caso*
   ```bash
   docker run -p 6000:5000 ismaelmrn/flask-app:latest
   # o con podman
   podman run -p 6000:5000 ismaelmrn/flask-app:latest
   ```
   
   Ahora accede a la app en [http://localhost:6000](http://localhost:6000)

## Subir a Docker Hub

1. Inicia sesión:
   ```bash
   docker login
   # o
   podman login docker.io
   ```
2. Sube la imagen:
   ```bash
   docker push ismaelmrn/flask-app:latest
   # o
   podman push ismaelmrn/flask-app:latest
   ```

---

¡Gracias por visitar este proyecto! Si te gusta, no dudes en dejar una estrella ⭐ en GitHub o contactar para cualquier colaboración.
