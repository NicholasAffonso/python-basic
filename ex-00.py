
# Lê inputs de tipo inteiro

value1 = int(input('type an integer number: '))
value2 = int(input('Type other integer number: '))

# Realiza as operações

soma = value1 + value2                     # Soma
subtrai = value1 - value2                  # Subtrai
multiply = value1 * value2                 # Multiplica
divide = value1 / value2                   # Divide
divide_recebe_inteiro = value1 // value2   # Divide e guarda o inteiro
divide_recebe_resto = value1 % value2     # Divide e guarda resto
exponencia = value1 ** value2              # exponencia

# Imprime os resultados

print('{} + {} = {} '.format(value1, value2, soma))                   # Mostra o resultado da soma
print('{} - {} = {} '.format(value1, value2, subtrai))                # Mostra o resultado da subtração
print('{} * {} = {} '.format(value1, value2, multiply))               # Mostra o resultado da multiplicação
print('{} / {} = {} '.format(value1, value2, divide))                 # Mostra o resultado da divisão
print('{} // {} = {} '.format(value1, value2, divide_recebe_inteiro)) # Mostra o inteiro da divisão
print('{} % {} = {} '.format(value1, value2, divide_recebe_resto))    # Mostra o resto da divisão
print('{} ** {} = {} '.format(value1, value2, exponencia))            # Mostra o resultado da exponênciação