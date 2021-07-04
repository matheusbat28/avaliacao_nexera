import funcao

class Registro_de_detalhe:

    def __init__(self, linha):
        self._linha = linha
        

    def mostrar_nome_fornecedor(self):
        return funcao.mostrador_de_codigo(self._linha, 43, 73)

    def mostrar_valor_pagamento(self):
        num = funcao.mostrador_de_codigo(self._linha, 119, 134)
        valor =int(num)
        return f"R${valor:.2f}"

    def numero_do_documento_atribuido_pela_a_empresa(self):
        return funcao.mostrador_de_codigo(self._linha, 73, 93)

    def data_pagamento(self):
        data = funcao.mostrador_de_codigo(self._linha, 93, 101)
        return f"{data[:2]}/{data[2:4]}/{data[4:]}      "

    def forma_lacramento(self):
        return "Credito em Conta Corrente"

    def __str__(self):
        return "| {}|{}|{} |{}                      |{}".format(
            self.mostrar_nome_fornecedor(),
            self.data_pagamento(),
            self.mostrar_valor_pagamento(),
            self.numero_do_documento_atribuido_pela_a_empresa(),
            self.forma_lacramento()
        )