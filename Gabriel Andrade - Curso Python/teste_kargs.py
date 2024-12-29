# def minha_funcao(*args, **kwargs):
#     for arg in args:
#         print(arg)
#     for key, value in kwargs.items():
#         print(key, value)
        
# minha_funcao (1,2,3,nome='Alice', idade=25)




palavras = ['gato', 'cachorro', 'elefante', 'leão', 'tigre','papagaio']


resultado = list(filter(lambda x: len(x) > 5, palavras))


print(resultado)