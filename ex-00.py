
# Lê inputs de tipo inteiro

val = int(input('type an integer number: '))
val2 = int(input('Type other integer number: '))

# Realiza as operações

som = val + val2        # Soma
sub = val - val2        # Subtrai
mul = val * val2        # Multiplica
div = val / val2        # Divide
div_int = val // val2   # Divide e guarda o inteiro
div_res = val % val2    # Divide e guarda resto
exp = val ** val2       # exponencia

# Imprime os resultados

print('{} + {} = {} '.format(val, val2, som))      # Mostra o resultado da soma
print('{} - {} = {} '.format(val, val2, sub))      # Mostra o resultado da subtração
print('{} * {} = {} '.format(val, val2, mul))      # Mostra o resultado da multiplicação
print('{} / {} = {:.3f} '.format(val, val2, div))  # Mostra o resultado da divisão
print('{} // {} = {} '.format(val, val2, div_int)) # Mostra o inteiro da divisão
print('{} % {} = {} '.format(val, val2, div_res))  # Mostra o resto da divisão
print('{} ** {} = {} '.format(val, val2, exp))     # Mostra o resultado da exponênciação