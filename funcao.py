from header_de_arquivo import Header_de_arquivos
from header_de_lote import  Header_de_lote
from registro_de_detalhes import Registro_de_detalhe
from trailer_de_aquivo import Trailer_de_arquivo
from trailer_de_lote import Trailer_de_lote

# função para ler o arquivo de entreda e amazenar em uma lista 
def lendo_arquivo_e_colocando_em_lista(arquivo, lista):
    for linha in arquivo:
        lista.append(linha)
    arquivo.close

# função para separar cada linha de lista em sua determinada classe
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

# função para capitar qual item no arquivo txt de entrada do sistema 
def mostrador_de_codigo(linha, primeiro_numero, segundo_numero):
    return linha[primeiro_numero:segundo_numero]

# função para capitar todas as informação do arquivo e mostrar na terminal 
def mostrar_na_tela(lista_registro_diferentes, lista_registro_iguais):
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

# função para capitar todas as informação do arquivo e arquivar em outro arquivo 
def arquivar_em_txt( lista_registro_diferentes, lista_registro_iguais):
    relatorio = open('relatorio.txt', 'w')

    relatorio.write("___________________________________________________________________________________________________________________________________________________________________________________________\n")
    relatorio.write("|Nome da Empresa               |Numero de Inscricao da Empresa|Nome do Banco                 |Nome da Rua                   |Numero do Local|Nome da Cidade      |CEP      |Sigla do Estado|\n")
    relatorio.write("___________________________________________________________________________________________________________________________________________________________________________________________\n")
    relatorio.write(f"{lista_registro_diferentes[0]}{lista_registro_diferentes[1]}\n")
    relatorio.write("___________________________________________________________________________________________________________________________________________________________________________________________\n")
    relatorio.write("__________________________________________________________________________________________________________________________________________\n")
    relatorio.write("|  Nome do Favorecido          |Data de Pagamento|Valor do Pagamento|Numero do Documento Atribuido pela Empresa|Forma de Lancamento      |\n")
    for x in lista_registro_iguais:
        relatorio.writelines(f"__________________________________________________________________________________________________________________________________________\n{x}\n__________________________________________________________________________________________________________________________________________")
