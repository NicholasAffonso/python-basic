# Lê tipo da variável

coisa = input('Digite alguma coisa: ')

# Imprime o tipo da variável

print('\n', type(coisa), '\n')

print('{:-^42}'.format(coisa))

# Imprimpe comparando com o método is

print('é alfanumérico?                    | ', coisa.isalnum())
print('é alfabético?                      | ', coisa.isalpha())
print('é ASCII?                           | ', coisa.isascii())
print('é decimal?                         | ', coisa.isdecimal())
print('é um dígito                        | ', coisa.isdigit())
print('pode ser usada como identificador? | ', coisa.isidentifier())
print('tudo em minúsculo?                 | ', coisa.islower())
print('tudo em maiúsculo?                 | ', coisa.isupper())
print('dá para imprimir?                  | ', coisa.isprintable())
print('é um título?                       | ', coisa.istitle())
print('é espaço em branco?                | ', coisa.isspace())