import json

class User:
    users = []

    def __init__(self, account: str, password: str, role: str):
        self.account = account
        self.password = password
        self.role = role

    def __str__(self):
        return f'Account: {self.account}, Role: {self.role}'

    @classmethod
    def load_users(cls, json_file: str = 'usuarios.json'):
        with open(json_file, 'r') as file:
            data = json.load(file)
            for user_data in data.get('Usuarios', []):
                user = User(user_data['account'], user_data['Password'], user_data['role'])
                cls.users.append(user)
    
    @classmethod
    def login(cls, account: str, password: str, role: str) -> None:
        for user in cls.users:
            if user.account == account:
                if user.password == password and user.role == role:
                    print("Login exitoso")
                    return True
                else:
                    print("Información inválida. Por favor, verifique.")
                    return False
        print("Cuenta no existente.")
        return False
