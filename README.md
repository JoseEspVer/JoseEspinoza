[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/lNPmxBXd)
# Laboratorio 1 - CS2031 🚀💯👩‍💻

¡Bienvenidos a la aventura inicial del curso CS2031! 🎓 En este laboratorio, nos sumergiremos en el fascinante mundo del desarrollo web, por esta primera semana aprovecharemos la simplicidad de FastAPI para comprender los conceptos e implementar lo aprendido en una API simple.

## 🎯 Propósito

El propósito de este laboratorio es doble: Por un lado, introducir a los estudiantes al uso de FastAPI, y por otro, proporcionarles las bases necesarias para crear una API desde las bases. Al concluir este laboratorio, los estudiantes tendrán en su haber habilidades esenciales en la manipulación de endpoints, estructuración de datos, y la realización de operaciones CRUD (Crear, Leer, Actualizar, Eliminar).

## 📖 Contexto

La conocida cafetería del sexto piso se ha convertido en un punto de encuentro clave para la comunidad universitaria. A pesar de su popularidad y la afluencia constante de estudiantes y profesores, se enfrenta a un reto mayor: la ausencia de un sistema digitalizado para el manejo eficiente del stock de sus productos.

En búsqueda de una solución innovadora, la administración de la cafetería ha confiado en el talento emergente de los estudiantes de CS2031 para desarrollar una API RESTful que mejore significativamente la gestión del inventario y, como consecuencia, optimice el servicio al cliente.

## 🛠️ Funcionalidades Requeridas

Para lograr una gestión eficaz, el sistema propuesto deberá permitir a los empleados de la cafetería ejecutar las siguientes acciones:

1. **Crear un producto**: Introducir nuevos productos en el sistema.
2. **Actualizar un producto**: Modificar la información de productos existentes.
3. **Eliminar un producto**: Remover del sistema aquellos productos que ya no se ofrezcan.
4. **Listar todos los productos**: Visualizar un catálogo completo de los productos disponibles.
5. **Listar un producto por su ID**: Acceder a la información detallada de un producto mediante su identificador único.

## 📋 Requerimientos de implementación

### ⚙️ Dependencias

Usa el siguiente comando para instalar las dependencias necesarias para el laboratorio:

```bash
pip install -r requirements.txt
```

### 📦 Estructura del recurso `Producto`


| Nombre | Tipo de dato | Descripción |
|--------|--------------|-------------|
| ID     | `UUID`         | Identificador único asignado a cada producto. |
| Nombre | `str`          | Designación comercial del producto. |
| Descripción | `str`     | Explicación breve del producto. |
| Precio | `float`        | Costo al que se ofrece el producto. |
| Stock  | `int`          | Cantidad disponible del producto en inventario. |


Usa el siguiente código para el modelo de los productos y no tener problemas con el testing:

```python
from pydantic import BaseModel
from typing import Optional
from uuid import uuid4, UUID

# Modelo para los productos
class Producto(BaseModel):
    id: Optional[UUID] = None
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    precio: Optional[float] = None
    stock: Optional[int]= None
```

### 🌐 Esquema de Endpoints

Para interactuar con el sistema, la API deberá implementar los siguientes puntos de acceso:

- `POST /productos`: Para el registro de nuevos productos.
- `PUT /productos/{id}`: Para la actualización integral de un producto específico.
- `PATCH /productos/{id}`: Para la actualización parcial de un producto.
- `DELETE /productos/{id}`: Para la eliminación de un producto.
- `GET /productos`: Para obtener un listado completo de los productos.
- `GET /productos/{id}`: Para consultar la información detallada de un producto mediante su ID.

### 🌟 Bonificaciones

Se valorarán positivamente funcionalidades adicionales tales como:

- `GET /productos/?stock=0`: Para listar productos con stock agotado.
- `POST /productos/{id}/comprar`: Para registrar la compra de un producto, reduciendo su stock en 1 unidad.
- `POST /productos/{id}/reponer`: Para aumentar el stock de un producto especificando la cantidad a añadir.

## 📝 Criterios de Evaluación

La evaluación de este laboratorio se basará en la correcta implementación de la API, siguiendo los criterios establecidos en la siguiente rúbrica de calificación, con una entrega a través de GitHub Classroom:

#### Endpoints Obligatorios

| Criterio | Puntos | Endpoint |
|----------|--------|-------------|
| Actualizar parcialmente un producto | 4 |  `PATCH /productos/{id}`. |
| Actualizar un producto | 4 |  `PUT /productos/{id}`. |
| Listar un producto por su ID | 3 |  `GET /productos/{id}`. |
| Crear un producto | 3 |  `POST /productos`. |
| Eliminar un producto | 3 |  `DELETE /productos/{id}`. |
| Listar todos los productos | 3 |  `GET /productos`. |
| **Total** | **20** | |

#### Endpoints Adicionales

| Criterio | Puntos | Endpoint |
|----------|--------|-------------|
| Listar productos sin stock | 1 | `GET /productos/?stock=0`. |
| Reponer stock | 2 | `POST /productos/{id}/reponer`. |
| Compra de producto | 1 | `POST /productos/{id}/comprar`. |

### 🚀 Consideraciones Finales
- Utilizar FastAPI para el desarrollo de la API.
- Almacenar la información de productos en una lista de diccionarios para facilitar su gestión.
- Asegurar que la API maneje eficientemente las solicitudes GET, POST, PUT, PATCH, y DELETE, demostrando una comprensión profunda de estas operaciones.

Este laboratorio no solo es una oportunidad para aprender sobre el desarrollo de APIs con FastAPI, sino también para contribuir a una solución real que mejore la operatividad de la cafetería universitaria. ¡Manos a la obra!