# TrabajoFinalSosaAlonso
Proyecto de página web pensada para organizar en una misma base de datos los registros importantes de los emprendimientos.

## Documentos

Este proyecto fue programado con lenguaje Python y utilizando framework Django.

Se descarga plantilla de bootstrap, la cual se modifica y adapta para el proyecto a presentar.

Se realizan herencias de padre a hijo renderizando las vistas en la plantilla utilizada.


## Vista Previa

[![Alt text](https://img.youtube.com/vi/yTI6dsJ3Nlg/0.jpg)](https://www.youtube.com/watch?v=yTI6dsJ3Nlg)

## Inicio

Encontraremos una primera vista general de la página web

## Archivos py:

#### models.py

Aquí encontramos el modelado de los objetos que se utilizaron para el proyecto y base de datos

#### forms.py

Se crearon los formularios necesarios para poder cargar datos en nuestra base de datos desde la página web

#### views.py

Son las vistas creadas a partir de nuestros modelos y formularios para navegar por la web

#### urls.py

Ubicación de las rutas utilizadas en el proyecto

## "Podes buscar un producto"

Es posible buscar productos, el programa consultará a nuestra base de datos si existe; de ser así, devolerá el producto buscado y el objeto al cual pertenece.


## Pasos para crear este proyecto. 

Se crea el nuevo proyecto utilizando python -m django startproject “Emprendimientos”.

Dentro del este proyecto se crea su aplicación (python -m django startapp App), y se registra dentro de settings en: INSTALLED_APPS.

Se desarrollan los modelos y sus atributos.

Se crean los formularios de dichos modelos (o clases) en un archivo forms.py dentro de la App del proyecto.

Se indica por consola que se creará una base de datos (python manage.py migrate)  y dentro se migran los modelos creados (python manage.py makemigrations).

Se descarga la plantilla bootstrap elegida, se realizan adaptaciones dentro de una carpeta llamada static de la aplicación (“App”) y se adapta el inicio al padre que heredarán sus hijos.

Se programan las views del proyecto y se realiza CRUD del modelo “proveedores”.

Se cargan las plantillas html para visualizar nuestro proyecto en la web, dentro de la carpeta “templates” de la aplicación (“App”).

Se configuran las rutas (urls necesarias) dentro de la aplicación (“App”)

Se configuran las rutas (urls necesarias) dentro del proyecto (“Emprendimientos”)

Se prueba el funcionamiento del framework utilizando: python manage.py runserver con éxito.
Se cargan datos de prueba en todos los formularios, guardado correctamente.

Se crea un usuario: python manage.py createsuperuser para utilizar el administrador de la aplicación.
Se ingresa correctamente al admin de la página web con el usuario y clave creados.

Dentro del archivo “admin.py” de la aplicación se crean los sitios de nuestros modelos para poder administrarlos .

Se confirma dentro del sitio de administración de Django que los modelos y sus datos se visualizan correctamente.

Se configura login, logout, registro y edición de perfil.
 
Se crea el modelo avatar y se adapta a cada vista creada.

Se realizan pruebas en la página web y sitio de administración, se confirma su completo y correcto funcionamiento.

Se sube el repositorio a GitHub.


## Autor

- Sosa Alonso Florencia Victoria
