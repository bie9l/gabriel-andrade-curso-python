numeros = []
impar = []
par = []



for i in range(10):
    valor = int(input("Digite um numero: "))
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)

print(f' Você digitou {len(par)} números pares, são eles: {par} ')
print(f' Você digitou {len(impar)} números impares são eles: {tuple(impar)} ')

print(f' A soma dos numeros pares é {sum(par)}, e a soma dos numeros impares é {sum(impar)}, e a soma de todos eles é {sum(par)+sum(impar)}.')


