#decimal
bits = raw_input('Dame un numero binario: ')

n = len(bits)

valor = 0

for bit in bits:
    if bit == '1':
        valor = valor + 2**(n-1)
    n -= 1

print 'Su valor decimal es:',valor
