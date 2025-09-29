# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

valor = multiplica(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(valor)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def valida_numero(numero):
    valida_numero_par = numero % 2 == 0

    if valida_numero:
        return f'O número {numero} é par.'
    return f'O numero {numero} é impar.'

print(valida_numero(10)) 