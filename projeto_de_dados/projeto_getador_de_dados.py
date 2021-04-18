'''
Seu projeto deve iniciar apresentando uma lista de opções sobre quais dado(s) devem ser gerados, pedindo o usuário
para escolher uma ou mais opções de dados a serem gerados entre as seguintes opções: gerar nome, gerar e-mail,
gerar telefone, gerar cidade, gerar estado, além de perguntar se os dados devem ser salvos para um arquivo também.
Finalmente o usuário deve poder digitar “parar” a qualquer momento para conseguir finalizar o programa.
'''
from random import choice, randint
nomes = ['Jose', 'Felipe', 'Douglas', 'maria', 'Julia', 'Jessica']
email = '@hotmail.com'
estado = ['Acre', 'Mato Grosso', 'Minas Gerais',
          'Rio de Janeiro', 'Rio Grande do Sul']
cidades = ['Rio Branco', 'Cuiabá', 'Belo horizonte',
           'Rio de Janeiro', 'Porto Alegre']
opcoes = []


def gerador_hotmail():
    nome = choice(nomes)
    print(nome + email)


def gerador_de_telefone():
    tele = []
    for numero in range(9):
        numeros = randint(1, 9)
        tele.append(numeros)
    telefone = f'9{tele[0]}{tele[1]}{tele[3]}{tele[4]}{tele[5]}{tele[6]}{tele[7]}{tele[8]}'
    print(telefone)


# tela principal
print(f'Escolha uma ou mais opções abaixo a serem geradas aleatóriamente:\n'
      f'[1] - Nome\n'
      f'[2] - E-mail\n'
      f'[3] - Telefone\n'
      f'[4] - Cidade\n'
      f'[5] - Estado\n')
opcoes = int(input('Digite uma(as) opções: '))
