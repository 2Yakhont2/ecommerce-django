# Tienda Online en django 

## Instrucciones para la instalación de paquetes

Para la instalación de paquetes debemos seguir las instrucciones a continuación:
- Abrir la carpeta con el IDE de preferencia
- Abrir la terminal y ejecutar el comando __python -m venv myapp__ . Este comando creara un entorno 
virtual llamado myapp.
- Ejecutar el entorno virtual: Desde la terminal abrimos la carpeta de 
nuestro recien creado entorno virtual, luego abrimos la carpeta Scripts y ejecutamos 
el archivo activate escribiendo ./activate.
- Regresamos a la ubicacion donde se encuentra el archivo requirements y ejecutamos
el comando: __pip install -r "requirements.txt"__ 

## Iniciar la aplicación 

En el paso anterior instalamos los paquetes necesarios para correr la aplicación, ahora
ejecutaremos tres comandos para mantener la integridad de los datos. 

- Abrir la carpeta ecom
- Ejecutar el comando __python manage.py makemigrations__
- Ejecutar el comando __python manage.py migrate__
- Iniciar la apliación: Ejecutar el comando __python manage.py runserver__
