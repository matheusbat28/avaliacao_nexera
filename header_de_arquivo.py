import funcao

# classe de arquivos Header_de_arquivos
class Header_de_arquivos:

# construtor da class Header_de_arquivos
    def __init__(self, linha):
        self._linha = linha

# método para capitar os numero de inscrição da empresa  
    def numero_de_inscricao_da_empresa(self):
        numero = funcao.mostrador_de_codigo(self._linha, 18, 32)
        return f"{numero[:2]}.{numero[2:5]}.{numero[5:8]}/{numero[8:12]}-{numero[12:]}"

# método para capitar o nome da empresa    
    def mostrador_do_nome_empresa(self):
        return funcao.mostrador_de_codigo(self._linha, 72, 102)

# método para capitar o nome do banco   
    def mostrador_do_nome_banco(self):
        return funcao.mostrador_de_codigo(self._linha, 102, 132)
    
# método str para moostrar o print da classe Header_de_arquivo
    def __str__(self):
        return "|{}|{}            |{}".format(
            self.mostrador_do_nome_empresa(),
            self.numero_de_inscricao_da_empresa(),
            self.mostrador_do_nome_banco()
            )