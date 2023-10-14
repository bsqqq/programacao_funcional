# Função lambda para cadastrar um novo usuário
cadastrar_usuario = lambda login: lambda senha: f'{login}:{senha}\n'

# Função lambda para verificar se o login e a senha estão corretos
fazer_login = lambda login: lambda senha: any(linha.strip() == f'{login}:{senha}' for linha in open('usuarios.txt'))

opcao = int(input("Digite 1 para cadastrar, 2 para fazer login: "))

login = input("Digite o login: ")
senha = input("Digite a senha: ")

main = lambda option: open('usuarios.txt', 'a').write(cadastrar_usuario(login)(senha)) and print("Usuário cadastrado com sucesso!") if option == 1 else (print("SUCESSO") if fazer_login(login)(senha) else print("FRACASSO")) if option == 2 else print("opção invalida")
main(opcao)