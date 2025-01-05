# Proyecto: Gestion de inventarios en Python

## Autor
- Yamila Ruggiero
- ruggieroyamila@gmail.com
- Talento tech - Comision 24216

## Descripción
Este proyecto es una aplicación simple de línea de comandos para gestionar tareas de un sistema de inventarios de la empresa Lumilagro SA. Permite añadir nuevos productos, listar los productos existentes, actualizar los productos y eliminar los mismos.

## Características
- Añadir nuevos productos con una identificacion unica,nombre,descripción,cantidad,precio,fecha de alta y categoria.
- Listar todos los productos con sus correspondientes categorias.
- Actualizar los datos de un producto deseado.
- Eliminar el producto deseado ingresando el codigo unico que lo identifica.
- Guardar los productos en una base de datos destinada al sistema de inventario.

## Requisitos
- Python 3.12.6 o superior.


## Estructura de Archivos
- main_final.py - contiene las funciones principales para ejecutar el programa.
- Funciones.py - contine las funciones para realizar las acciones necesarias del programa. registrs,actualizar,listar y eliminar. por otro lado, contiene las funciones para conectar con la DB.
- inventariolumilagro.db - contine los datos del sistema, DB sqlite3 
