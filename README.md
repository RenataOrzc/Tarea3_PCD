# FastAPI User Management API
#### *Descripción*
Este proyecto es una API RESTful construida con FastAPI que permite gestionar usuarios en una base de datos. La API soporta operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para los usuarios y utiliza SQLAlchemy para interactuar con la base de datos.

Funcionalidades
Crear Usuario: Añadir un nuevo usuario con atributos como nombre, correo electrónico, edad, recomendaciones y código postal.
Leer Usuarios: Obtener una lista de todos los usuarios almacenados en la base de datos.
Actualizar Usuario: Modificar la información de un usuario existente.
Eliminar Usuario: Borrar un usuario de la base de datos por su ID.
<br>
#### **Estructura del Proyecto**
main.py: Archivo principal que define y expone los endpoints de la API.
models.py: Contiene los modelos de SQLAlchemy que definen la estructura de la base de datos.
database.py: Configura la conexión a la base de datos y las sesiones de SQLAlchemy.