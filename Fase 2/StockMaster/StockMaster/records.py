import json
from datetime import datetime
import os

class Record:
    def __init__(self,Record_id, id, amount, movement):
        now = datetime.now()
        self.Record_id = Record_id
        self.Product_id = id
        self.Amount = amount
        self.Movement = movement
        self.Date = now.strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            'Record_id': self.Record_id,
            'Product_id': self.Product_id,
            'Amount': self.Amount,
            'Movement': self.Movement,
            'Date': self.Date
        }

    @classmethod
    def create_empty_json(cls, json_file='records.json'):
        if not os.path.exists(json_file):
            with open(json_file, 'w') as file:
                data = {'Registros': []}
                json.dump(data, file, indent=4)
            print(f"Archivo JSON vacío creado en {json_file}")
        else:
            pass

    @classmethod
    def get_next_id(cls, json_file='records.json'):
        if os.path.exists(json_file):
            with open(json_file, 'r') as file:
                data = json.load(file)
                if data['Registros']:
                    last_record = data['Registros'][-1]
                    return last_record['Record_id'] + 1
                else:
                    return 1
        else:
            return 1

    @classmethod
    def add_record_to_json(cls, product_id, amount, movement, json_file='records.json'):
        next_id = cls.get_next_id(json_file)
        record = Record(next_id, product_id, amount, movement)
        
        try:
            with open(json_file, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {'Registros': []}
        
        data['Registros'].append(record.to_dict())

        with open(json_file, 'w') as file:
            json.dump(data, file, indent=4)

