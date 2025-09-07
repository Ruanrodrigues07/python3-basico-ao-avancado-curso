nome = 'Ruan Rodrigues'
altura = 1.79
peso = 70
imc = float(peso / altura ** 2)

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Ruan Rodrigues tem 1.79 de altura,
# pesa 70 quilos e seu imc é        
# 21.847008520333322