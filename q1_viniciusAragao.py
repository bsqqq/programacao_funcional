users = {
    "vinicius": 123456,
    "lincoln": 987654,
    "admin": 999999999,
    "test": 000000000
}

amount = {
    "vinicius": 0.54,
    "lincoln": 999.99,
    "admin": 999999.0,
    "test": 0
}
usernames = list(users.keys())

user = input("Username: ")
password = int(input("Password: "))

login = lambda usr, passw: list(users.keys())[usernames.index(user)] if usr in users.keys() and passw == users[usr] else False

print(f'Bem vindo {login(user, password)}') if login(user, password) else None
authenticated = login(user, password) if login(user, password) else print("Login invalido, tente novamente")
exit() if not authenticated else None

withdrawal = lambda auth: lambda quantia: lambda howMuch: quantia - howMuch if quantia >= howMuch and auth else print("Não é possível sacar")
deposit = lambda auth: lambda quantia: lambda howMuch: quantia + howMuch if auth else print("Não é possível depositar")

print("Selecione uma ação:") 
print("1 - Sacar") 
print("2 - Depositar")

action = int(input())
quanto = float(input("Quanto? "))
print(withdrawal(authenticated)(amount[authenticated])(quanto)) if action == 1 else print(deposit(authenticated)(amount[authenticated])(quanto)) if action == 2 else print("Ação inválida")
