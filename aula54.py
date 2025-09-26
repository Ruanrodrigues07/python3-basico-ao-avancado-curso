"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista_de_compras = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':

        os.system('cls') 
        
        item = input('Digite o item: ')
        lista_de_compras.append(item)
        print(f'"{item}" foi adicionado à lista.')

    elif opcao == 'a':
        os.system('cls')

        if len(lista_de_compras) == 0:
            print('A lista de compras está vazia. Não há nada para apagar.')
            continue # Volta para o início do loop

        # Mostra a lista para o usuário saber qual índice apagar
        print('Qual item você deseja apagar?')
        for indice, item in enumerate(lista_de_compras):
            print(indice, '-', item)

        try:
            # A variável que recebe o input é 'indice_para_apagar'
            indice_para_apagar = int(input('Digite o índice do item: '))
            
            # Remove o item usando a variável correta
            item_removido = lista_de_compras.pop(indice_para_apagar)
            print(f'"{item_removido}" foi removido da lista.')

        # Captura erros de valor
        except ValueError:
            print('Erro: Por favor, digite um número de índice válido.')
        # Captura erros de índice
            print('Erro: O índice informado não existe na lista.')
        # Captura qualquer outro erro inesperado
        except Exception as e:
            print(f'Ocorreu um erro inesperado: {e}')

    elif opcao == 'l':
        os.system('cls')

        if len(lista_de_compras) == 0:
            print('A lista de compras está vazia.')

        else:
            print('--- Sua Lista de Compras ---')
            for indice, item in enumerate(lista_de_compras):
                print(indice, '-', item)
            print('--------------------------')

    else:
        print('Opção inválida. Por favor, escolha "i", "a" ou "l".')