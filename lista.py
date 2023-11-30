# Programa para exibir uma lista de informação para o usuário 

print('Consultor de ingredientes')

bolo = ['trigo', 'ovo', 'açúcar', 'chocolate em pó', 'fermento químico']
pao = ["trigo", 'ovo', 'açúcar', 'manteiga', 'sal']

print('\nDigite 1 para bolo 2 para pão e 0 para sair')

usua = input("Digite a opção: ")

while usua != '0':
    
    if usua == "1":
        print('\nAqui estão os ingredientes para o preparo de um bolo:')
        for i in bolo:
            print(i)

    elif usua == "2":
        print('\nAqui estão os ingredientes para o preparo de um pão:')
        for e in pao:
            print(e)

    elif usua == "0":
        print("\nSaindo...")
        exit()

    elif usua != ('0', '1', '2'):
        print("\nOpção inválida")

    print('\nSe deseja consultar novamente mais aulguma receita digite 1 para bolo 2 para pão e 0 para sair')
    
    usua = input("Digite a opção: ")
