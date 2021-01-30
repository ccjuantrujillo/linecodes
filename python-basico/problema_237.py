letra = raw_input('Dame una letra: ')

if (len(letra)== 1 and 'a'<=letra<='z') or letra in [chr(160),chr(130),chr(161),chr(162),chr(163),chr(164)] :
    print letra , 'es una letra minuscula'
    
print chr(160)
print chr(130)
print chr(161)
print chr(162)
print chr(163)
print chr(164)