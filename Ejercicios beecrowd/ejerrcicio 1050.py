marcación_telefónica = {
    61: 'Brasilia',
    71: 'Salvador',
    11: 'Sao Paulo',
    21: 'Rio de Janeiro',
    32: 'Juiz de Fora',
    19: 'Campinas',
    27: 'Vitoria',
    31: 'Belo Horizonte',
}
DDD = int(input(""))

if DDD in marcación_telefónica:
    print(marcación_telefónica[DDD])
else:
    print("DDD nao cadastrado")