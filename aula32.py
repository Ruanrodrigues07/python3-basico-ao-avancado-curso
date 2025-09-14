"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# Resolução 1

# entrada = input('Digite um número inteiro: ')

# try:
#     entrada_int = int(entrada)
#     valida_numero = entrada_int % 2 == 0

#     par_ou_impar = 'impar'

#     if valida_numero:
#         par_ou_impar = 'par'

#     print(f'O número {entrada_int} é {par_ou_impar}')

# except:
#     print('O você digitou um número que não é inteiro.')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# Resolução 2

# entrada = input('Digite quais horas são: ')

# entrada_int = int(entrada)

# try:

#     if entrada_int <= 11:
#         print('Bom dia!!')
#     elif entrada_int <= 17:
#         print('Boa tarde')
#     else:
#         print('Boa noite')

# except:
#     print('Digite apenas número inteiros')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# Resolução 3

nome = input('Digite o seu primeiro nome: ')

tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print('Seu nome é curto')
elif tamanho_nome <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
