from operacoesbd import *
#1 listar, 2 adicionar filme, 3 sair

opcao = 123
filmes = [ ]
conn = abrirBancoDados('127.0.0.1','root','R@malho76899r','locadora CineHome')

while opcao != 3:
    print('Locadora CineHome')
    print('1 listar, 2 adicionar filme, 3 sair')
    opcao = int(input('Digite a sua opção: '))

    if opcao == 1:
        print('Lista de Filmes')
        consultaSqlListagemFilmes = 'select * from filme'
        filmes = listarBancoDados(conn, consultaSqlListagemFilmes)

        for f in filmes:
            print(f)

    elif opcao == 2:

        nomeFilme = input('nome do filme: ')
        sinopseFilme = input('sinopse do filme: ')
        anoFilme = int(input('ano do filme: '))

        consultaInsertFilme = 'insert into filme (titulo,sinopse,ano) values(%s,%s,%s)'
        dados = [nomeFilme, sinopseFilme, anoFilme]

        insertNoBancoDados(conn, consultaInsertFilme, dados)
        print('Filme adicionado com sucesso!')

    elif opcao != 3:
        print('Opcao Invalida!')

encerrarBancoDados(conn)
print('Obrigado por usar a Locadora')

