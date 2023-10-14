from flask import Flask, request, render_template
app = Flask(__name__, template_folder='templates_folder')

# Função lambda para cadastrar um novo usuário
cadastrar_usuario = lambda login: lambda senha: f'{login}:{senha}\n'

# Função lambda para verificar se o login e a senha estão corretos
fazer_login = lambda login: lambda senha: any(linha.strip() == f'{login}:{senha}' for linha in open('usuarios.txt'))

opcao = int(input("Digite 1 para cadastrar, 2 para fazer login: "))

login = input("Digite o login: ")
senha = input("Digite a senha: ")

main = lambda option: open('usuarios.txt', 'a').write(cadastrar_usuario(login)(senha)) and print("Usuário cadastrado com sucesso!") if option == 1 else (print("SUCESSO") if fazer_login(login)(senha) else print("FRACASSO")) if option == 2 else print("opção invalida")
main(opcao)

welcome = lambda: f'WELCOME {request.form["username"]}!!'
wrong = lambda: "WRONG PASSWORD!!!!"
invalid = lambda: "User does not exist!"

# password_matches = lambda dic: dic[f'{request.form["username"]}'] == f'{request.form["password"]}'

check_password = lambda: welcome() if fazer_login(f'{request.form["username"]}')(f'{request.form["password"]}') else wrong()
check_if_user_exists = lambda: check_password() if f'{request.form["username"]}' in open('usuarios.txt', 'r').read() else invalid()

reqresp = lambda: check_if_user_exists() if request.method == "POST" else render_template("index.html")

app.add_url_rule("/index/", "index", reqresp, methods=["GET", "POST"])
app.run(host="0.0.0.0", port=8080)