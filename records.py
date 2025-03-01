import json
from datetime import datetime
import os

class Record:
    # Constructor de la clase Record
    def __init__(self,Record_id, id, amount, movement):
        now = datetime.now()    # Fecha y hora actual
        self.Record_id = Record_id              # Identificador del registro
        self.Product_id = id                    # Identificador del producto
        self.Amount = amount                    # Cantidad
        self.Movement = movement                # Movimiento
        self.Date = now.strftime("%Y-%m-%d")    # Fecha

    # Convierte el registro a un diccionario
    def to_dict(self):
        return {
            'Record_id': self.Record_id,
            'Product_id': self.Product_id,
            'Amount': self.Amount,
            'Movement': self.Movement,
            'Date': self.Date
        }

    # Inicializa un archivo JSON
    @classmethod
    def initialize_json_file(cls, json_file='records.json'):   
        if not os.path.exists(json_file):   # Verifica si el archivo no existe
            with open(json_file, 'w') as file:  # Abre el archivo en modo escritura
                data = {'Registros': []}    # Crea un diccionario vacío
                json.dump(data, file, indent=4)   # Escribe el diccionario en el archivo JSON
            print(f"Archivo JSON vacío creado en {json_file}") 

    # Obtiene el siguiente identificador
    @classmethod
    def get_next_id(cls, json_file='records.json'):
        if os.path.exists(json_file):   # Verifica si el archivo existe
            with open(json_file, 'r') as file:  # Abre el archivo en modo lectura
                data = json.load(file)  # Carga el archivo JSON
                if data['Registros']:   
                    last_record = data['Registros'][-1] # Obtiene el último registro
                    return last_record['Record_id'] + 1  # Retorna el siguiente identificador
                else:
                    return 1
        else:
            return 1

    # Agrega un registro al archivo JSON
    @classmethod
    def add_record_to_json(cls, product_id, amount, movement, json_file='records.json'):
        next_id = cls.get_next_id(json_file)    # Obtiene el siguiente identificador
        record = Record(next_id, product_id, amount, movement)  # Crea un objeto de la clase Record
        
        try:
            with open(json_file, 'r') as file:  # Abre el archivo en modo lectura
                data = json.load(file)  # Carga el archivo JSON
        except FileNotFoundError:
            data = {'Registros': []}    # Crea un diccionario vacío  
        
        data['Registros'].append(record.to_dict())  # Agrega el registro al diccionario

        with open(json_file, 'w') as file:  # Abre el archivo en modo escritura
            json.dump(data, file, indent=4)  # Escribe el diccionario en el archivo JSON

