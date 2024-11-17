##Dicionario

#notas_medias = [6.8, 8.0, 7.0, 8.7, 5.6, 6.9, 9.2, 8.4, 9.3, 10]

#problema, se tirou >7 aprovado, se nao reprovado

#for nota in notas_medias:
#    if nota >= 7:
#        print('Aprovado')
#    else:
#        print('Reprovado')


#perfil = {
#    "nome": 'Banana',
#    "ano_de_entrada": 2024,
#    "previsao_de_formatura": 2026,
#
#}
    

# Calcule a media das idades ,se a media das idades for:
# Menor que 25, o programa deverá imprimir: é um grupo jovém.
# Entre 25 e 60, o programa deverá imprimir: é um grupo adulto.
# Se for maior 60, o programa deverá imprimir: é um grupo idoso.



# idade = [6, 23, 14, 88, 53, 36, 65, 32, 11, 8, 16, 24]

# media = sum(idade)/len(idade)

# print(media)

# if media < 25:
#     print('É um grupo jovem')
# elif media >= 25 and media <= 60:
#     print('É um grupo adulto')
# elif media > 60:
#     print('É um grupo idoso')



# numero = int(input('Digite o numero: '))

# if numero % 2 == 0:
#     print('Numero par')
# else:
#     print('Numero impar')


#36 - Crie um algoritmo que ao ser executado recebe uma palavra, verifica se a palavra se inicia com uma vogal
# e exibe a mensagem "Começa em vogal" caso a palavra se inicie em vogal
# ou exibe a mensagem "Começa em consoante" caso a palavra não se inicie em vogal


palavra = input('Digite uma palavra: ')

if palavra[0] in ['a','e','i','o','u','A','E','I','O','U']:
    print('Começa em vogal')
else:
    print('Começa em consoante')
