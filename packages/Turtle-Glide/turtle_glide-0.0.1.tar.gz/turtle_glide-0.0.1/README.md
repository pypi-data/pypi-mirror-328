# Turtle Glide
=====================================

## Comando `create_archive.py`
-----------------------------

El comando `create_archive.py` se utiliza para crear un archivo HTML dentro de la carpeta `templates` o `static` de una aplicación.

### Argumentos
---------------

* `app_name`: Nombre de la aplicación
* `file_path`: Ruta del componente
* `--type`: Tipo de archivo a crear. Las opciones son:
	+ `template` para archivos en la carpeta `templates`
	+ `static` para archivos en la carpeta `static`
* De manera predeterminada, si no se especifica el tipo, se colocará en la carpeta `templates`.

### Ejecución
--------------

* El comando recupera la configuración del `app_name` especificado.
* Crea los directorios necesarios si no existen.
* Verifica si el archivo ya existe y proporciona una advertencia si es así.
* Dependiendo de la extensión del archivo, rellena el archivo con contenido predeterminado.

### Ejemplos de uso
--------------------

```bash
python3 manage.py create_archive accounts user/dialog.html
```

```bash
python3 manage.py create_archive accounts css/user/user.css --type=static
```

Al ejecutar el comando, se generará el archivo especificado en el directorio correspondiente y se mostrará un mensaje de éxito al finalizar.