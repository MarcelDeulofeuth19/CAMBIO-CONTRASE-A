# Cambiar Contraseña - Mini App

Este es un mini aplicativo para solicitar el cambio de contraseña, inspirado en el diseño de la plataforma AlóCredit.

## ¿Cómo funciona?
- El usuario ingresa su correo electrónico.
- Al enviar el formulario, se hace una petición POST al endpoint:
  
  `http://98.91.0.246:3000/journey-notification`
  
  con el siguiente JSON:
  ```json
  {
    "variable1": "user@example.com",
    "variable2": "2"
  }
  ```
- Si la petición es exitosa, se muestra un mensaje de confirmación.

## Instrucciones para correr con Docker

1. Ve a la carpeta `app`:
   ```sh
   cd app
   ```
2. Construye la imagen:
   ```sh
   docker build -t cambio-contrasena-app .
   ```
3. Ejecuta el contenedor:
   ```sh
   docker run -p 5000:5000 cambio-contrasena-app
   ```
4. Abre tu navegador en [http://localhost:5000](http://localhost:5000)

---

**Notas:**
- El diseño replica el fondo y estilo del login original.
- Solo se requiere el correo electrónico para solicitar el cambio.
- El endpoint y el valor de `variable2` están fijos según lo solicitado.
