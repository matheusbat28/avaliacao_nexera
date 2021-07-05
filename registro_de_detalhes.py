import funcao

# classe Registro_de_detalhe
class Registro_de_detalhe:

# construtor da classe Registro_de_detalh
    def __init__(self, linha):
        self._linha = linha
        
# método para capitar o nome do fornecedor
    def mostrar_nome_fornecedor(self):
        return funcao.mostrador_de_codigo(self._linha, 43, 73)

# método para capitar o valor do pagamento 
    def mostrar_valor_pagamento(self):
        num = funcao.mostrador_de_codigo(self._linha, 119, 134)
        valor =int(num)
        return f"R${valor:.2f}"

# método para capitar o numero atribudo pela empresa 
    def numero_do_documento_atribuido_pela_a_empresa(self):
        return funcao.mostrador_de_codigo(self._linha, 73, 93)

# método para capitar a data do pagamento e formatado com padrão da empresa 
    def data_pagamento(self):
        data = funcao.mostrador_de_codigo(self._linha, 93, 101)
        return f"{data[:2]}/{data[2:4]}/{data[4:]}      "

# método para capitar a data do pagamento e formatado com padrão da empresa 
    def forma_lacramento(self):
        return "Credito em Conta Corrente"

# método str para mostrar o print da classe Registro_de_detalhe
    def __str__(self):
        return "| {}|{}|{} |{}                      |{}".format(
            self.mostrar_nome_fornecedor(),
            self.data_pagamento(),
            self.mostrar_valor_pagamento(),
            self.numero_do_documento_atribuido_pela_a_empresa(),
            self.forma_lacramento()
        )