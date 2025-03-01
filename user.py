import os
import json

class User:
    users = []  # Lista de usuarios

    # Constructor de la clase User
    def __init__(self, account: str, password: str, role: str): 
        self.account = account
        self.password = password
        self.role = role

    # Retorna la cuenta y el rol del usuario
    def __str__(self):  
        return f'Account: {self.account}, Role: {self.role}'    

    # Carga los usuarios desde un archivo JSON
    @classmethod 
    def load_users(cls, json_file: str = 'usuarios.json'):  # Carga los usuarios desde un archivo JSON
        base_dir = os.path.dirname(os.path.abspath(__file__))   # Directorio base
        file_path = os.path.join(base_dir, json_file)   # Ruta del archivo JSON

        try:
            with open(file_path, 'r') as file:  # Abre el archivo en modo lectura
                data = json.load(file)  # Carga el archivo JSON
                for user_data in data.get('Usuarios', []):  # Recorre los datos de los usuarios
                    user = User(    # Crea un objeto de la clase User
                        user_data['account'], user_data['Password'], user_data['role']
                        )
                    cls.users.append(user)  # Agrega el usuario a la lista
            print(f"Users successfully loaded from '{file_path}'")

        except FileNotFoundError:
            print(f"Error: File '{file_path}' does not exist")
        except json.JSONDecodeError:
            print(f"The file '{file_path}' is corrupt or is not a valid JSON")
    
    # Verifica las credenciales del usuario
    @classmethod
    def login(cls, account: str, password: str, role: str) -> None:
        for user in cls.users:  # Recorre la lista de usuarios
            if user.account == account:     # Verifica si la cuenta existe
                # Verifica la contraseña y el rol
                if user.password == password and user.role == role:     
                    print("Successful login")
                    return True
                else:
                    print("Invalid information")
                    return False
        print("Account does not exist")
        return False
