import funcao

# classe de header de lote
class Header_de_lote:

#construtor da class  Header_de_lote
   def __init__(self, linha):
      self._linha = linha

# método para capitar o logradouro
   def mostrar_logradouro(self):
      return funcao.mostrador_de_codigo(self._linha, 142, 172)

# método para capitar o número do local 
   def mostrar_numero_local(self):
      return funcao.mostrador_de_codigo(self._linha, 172, 177)
      
# método para capitar o nome da cidade
   def mostrar_nome_cidade(self):
      return funcao.mostrador_de_codigo(self._linha, 192, 212)

# método para capitar o cep e formatado no padrão pedido
   def mostra_cep(self):
      cep = funcao.mostrador_de_codigo(self._linha, 212, 220)
      return f"{cep[:5]}-{cep[5:]}"

# método para capitar a sigla do estado
   def mostrar_sigla_estado(self):
      return funcao.mostrador_de_codigo(self._linha, 220, 222)

# método str para moostrar o print da classe Header_de_arquivo
   def __str__(self):
      return "|{}|{}          |{}|{}|{}             |".format(
         self.mostrar_logradouro(),
         self.mostrar_numero_local(),
         self.mostrar_nome_cidade(),
         self.mostra_cep(),
         self.mostrar_sigla_estado()
      )