from header_de_arquivo import Header_de_arquivos
from header_de_lote import  Header_de_lote
from registro_de_detalhes import Registro_de_detalhe
from trailer_de_aquivo import Trailer_de_arquivo
from trailer_de_lote import Trailer_de_lote

def lerdo_arquivo_e_colocando_em_lista(arquivo, lista):

    for linha in arquivo:
        lista.append(linha)
    arquivo.close

def separador_arquivo(lista, lista_registro_iguais, lista_registro_diferentes):
    intem = 0
    while intem < len(lista):
        if lista[intem][7:8] == "0":
            lista_registro_diferentes.append(Header_de_arquivos(lista[intem]))
        elif lista[intem][7:8] == "1":
            lista_registro_diferentes.append(Header_de_lote(lista[intem]))
        elif lista[intem][7:8] == "3":
            lista_registro_iguais.append(Registro_de_detalhe(lista[intem]))
        elif lista[intem][7:8] == "5":
            lista_registro_diferentes.append(Trailer_de_lote(lista[intem]))
        elif lista[intem][7:8] == "9":
            lista_registro_diferentes.append(Trailer_de_arquivo(lista[intem]))
        intem += 1

def mostrador_de_codigo(linha, primeiro_numero, segundo_numero):
    return linha[primeiro_numero:segundo_numero]

def capitador_de_codigo(linha, primeiro_numero, segundo_numero):
    return linha[primeiro_numero:segundo_numero]

