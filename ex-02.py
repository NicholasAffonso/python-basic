# Exibe ordem de precedência

tit_ord = 'Ordem de precedência'

print('\n {:-^45} \n'.format(tit_ord))

print(' 1º | ()          Tudo que está entre parênteses \n 2º | **          Exponenciação \n 3º | * / // %    Na orden que aparecer \n 4º | + - \n')

# Pede um valor

val = int(input('Digite um alor: '))

# Exibe o antecessor e sucessor

print('\nAntecessor = {} \nSucessor = {}'.format(val - 1, val + 1))

# Exibe o dobro, triplo e raiz quadrada do valor

print('\nO dobro de {} é {}'.format(val, val * 2))
print('O triplo de {} é {}'.format(val, val * 3))
print('A raiz quadrada de {} é {:.2f}'.format(val, val ** (1/2)))