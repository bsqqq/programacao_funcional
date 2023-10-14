# Função lambda para cadastrar um novo usuário
cadastrar_usuario = lambda login: lambda senha: f'{login}:{senha}\n'

# Função lambda para verificar se o login e a senha estão corretos
fazer_login = lambda login: lambda senha: any(linha.strip() == f'{login}:{senha}' for linha in open('usuarios.txt'))

opcao = input("Digite 1 para cadastrar, 2 para fazer login: ")

if opcao == '1':
    novo_login = input("Digite o novo login: ")
    nova_senha = input("Digite a nova senha: ")
        
    with open('usuarios.txt', 'a') as file:
        file.write(cadastrar_usuario(novo_login)(nova_senha))
    print("Usuário cadastrado com sucesso!")

elif opcao == '2':
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")
    print("SUCESSO") if fazer_login(login)(senha) else print("FRACASSO")

else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")
