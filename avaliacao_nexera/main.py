from typing import List
import funcao

lista = []
lista_registro_iguais = []
lista_registro_diferentes = []

arquivo = open('modelo_arquivo.txt', 'r')

funcao.lerdo_arquivo_e_colocando_em_lista(arquivo, lista)
funcao.separador_arquivo(lista, lista_registro_iguais, lista_registro_diferentes)

print("___________________________________________________________________________________________________________________________________________________________________________________________")
print("|Nome da Empresa               |Numero de Inscricao da Empresa|Nome do Banco                 |Nome da Rua                   |Numero do Local|Nome da Cidade      |CEP      |Sigla do Estado|")
print("___________________________________________________________________________________________________________________________________________________________________________________________")
print(f"{lista_registro_diferentes[0]}{lista_registro_diferentes[1]}")
print("___________________________________________________________________________________________________________________________________________________________________________________________")



print("__________________________________________________________________________________________________________________________________________")
print("|  Nome do Favorecido          |Data de Pagamento|Valor do Pagamento|Numero do Documento Atribuido pela Empresa|Forma de Lancamento      |")
for x in lista_registro_iguais:
    print("__________________________________________________________________________________________________________________________________________")
    print(x)
print("__________________________________________________________________________________________________________________________________________")


                               