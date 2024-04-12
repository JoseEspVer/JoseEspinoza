from pydantic import BaseModel
from typing import Optional
from uuid import uuid4, UUID
from fastapi import FastAPI, HTTPException,Response


app = FastAPI()

# Modelo para los productos
class Producto(BaseModel):
    id: Optional[UUID] = None
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    precio: Optional[float] = None
    stock: Optional[int]= None

productos=[]

@app.post("/productos")
def crear_producto(producto:Producto):
    producto.id=uuid4()
    productos.append(producto)
    return producto

@app.put("/productos/{producto_id}",response_model=Producto)
def actualizar_producto_total(producto_id:UUID, datos_parciales: dict):
    for p in productos:
        if p.id == producto_id:
            for field, value in datos_parciales.items():
                setattr(p, field, value)
                return p
    raise HTTPException(status_code=404, detail="Producto no encontrado")


@app.patch("/productos/{producto_id}",response_model=Producto)
def actualizar_producto_parcialmente(producto_id:UUID, datos_parciales: dict):
    for p in productos:
        if p.id == producto_id:
            for field, value in datos_parciales.items():
                setattr(p, field, value)
                return p
    raise HTTPException(status_code=404, detail="Producto no encontrado")

@app.delete("/productos/{producto_id}", response_model=Producto)
def eliminar_producto(producto_id:UUID):
    for j in productos:
        if j.id == producto_id:
            productos.remove(j)
        raise HTTPException(status_code=204, detail="Producto suprimido")
    raise HTTPException(status_code=404, detail="Producto no encontrado")

@app.get("/productos")
def listar_todos_los_productos():
    return productos

@app.get("/productos/{productos_id}",response_model=Producto)
def consultar_producto_por_id(productos_id:UUID):
    for i in productos:
        if i.id==productos_id:
            return i
    raise HTTPException(status_code=404, detail="Producto no encontrado")    