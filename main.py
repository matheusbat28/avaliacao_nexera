import funcao

lista = []
lista_registro_iguais = []
lista_registro_diferentes = []

arquivo = open('modelo_arquivo.txt', 'r')

funcao.lendo_arquivo_e_colocando_em_lista(arquivo, lista)
funcao.separador_arquivo(lista, lista_registro_iguais, lista_registro_diferentes)
funcao.mostrar_na_tela(lista_registro_diferentes, lista_registro_iguais)
funcao.arquivar_em_txt(lista_registro_diferentes,lista_registro_iguais)                            
                             