##Universidad nacional e informacion del curso***
![By (Doc Banner)](https://github.com/user-attachments/assets/849f0868-f4eb-493d-b6d7-1d115af4b103)

> Sistema de gestión de inventario para una tienda de productos y componentes electrónicos, propuesto como proyecto final para la asignatura POO



## 🚀 Funcionalidades propuestas
- ✅ Carga masiva de datos desde una base .json
- ✅ Mostrar el inventario actualizado en cualquier momento
- ✅ Consulta detallada de cada operación (fecha, hora, usuario)
#Fase 1
carreta de la fase 1

## 🏗 Diagrama UML

```mermaid
classDiagram
    class Producto {
        - id_producto: str
        - nombre: str
        - precio: float
        - cantidad: int
        + __init__(id_producto, nombre, categoria, precio, cantidad)
        + to_dict() dict
        + from_dict(data: dict) Producto
    }

    class Registro {
        - id_registro: int
        - id_producto: str
        - cantidad: int
        - tipo: str
        - fecha: str
        + __init__(id_registro, id_producto, cantidad, tipo, fecha)
        + to_dict() dict
    }

    class Inventario {
        - productos: list~Producto~
        - registros: list~Registro~
        + __init__()
        + agregar_producto(id_producto, nombre, precio, cantidad) "Crea registro automáticamente"
        + registrar_entrada(id_producto, cantidad)  "Crea registro automáticamente"
        + registrar_salida(id_producto, cantidad)  "Crea registro automáticamente"
        + listar_inventario()
        + buscar_producto(id_producto) Producto
    }

    Inventario --> Producto : 
    Inventario --> Registro : 
```


## 🛠 Estructura de archivos

```plaintext
📦 StockMaster/
|── 📌 main.py                    # Punto de entrada del programa
|
│── 📂 models/                    # Clases principales del proyecto
|  |── 📌 product.py              # Clase Producto: representa los productos del inventario
|  |── 📌 records.py              # Clase Registro: representa los movimientos (entradas/salidas)
|
│── 📂 services/                  # Lógica de negocio
|  |── 📌 inventory_service.py    # Manejo de inventario, registros y persistencia
|
│── 📄 products.json              # Archivo para almacenar los datos de los productos
│── 📄 records.json               # Archivo para almacenar los movimientos de inventario
│
│── 📄 README.md                  # Documentación del proyecto
```

##resultados fase 1
aqui deberíamos poner evidencias de como funciona la consola. lo que hizo julian

#Fase 2
##resultados fase 2
La primera interacción con el usuario es el ingreso al sistema
```python
Welcome to StockMaster
Please login
Name: juanito perez
Password: 1144
Role: employee
Cuenta no existente.
```
juanito perez no es un trabajador de la empresa ni está registrado en el sistema

```python
Welcome to StockMaster
Please login
Name: Felipe Gonzalez
Password: 0000
Role: Employee
Información inválida. Por favor, verifique.
```
Felipe Gonzalez está en el sistema pero su ingreso no correponde con los datos regitrados en la base de seguridad.
```python
Welcome to StockMaster
Please login
Name: Felipe Gonzalez
Password: 0000
Role: Boss
Login exitoso

Welcome to our sistem. Select an option:
1. Add product
2. Show products
3. Search product
4. Change stock
5. Update product
6. Delete product
7. Exit
Select an option: 1
Enter product id: 1000
Enter product name: Digital Camera
Enter product price: 2800
Enter product stock: 3
Product added successfully
Welcome to StockMaster
Please login
Name:

```
La información coincide con la base de datos de seguridad y el Jefe pudo ingresar al sistema. allí logra entrar a lo que se evidenció en la fase 1

## 🌟 Integrantes  
- 📱 Amaya Gómez Ana María
- 🏭 Daza Yepes Santiago
- 🤖 Torres Zaque Julian Ricardo


---

