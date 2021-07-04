import funcao

# classe de header de lote
class Header_de_lote:

#inciador da class  Header_de_lote
   def __init__(self, linha):
      self._linha = linha

   def mostrador_de_forma_de_lancamento(self):
      return funcao.mostrador_de_codigo(self._linha, 11, 13)

   def mostrar_logradouro(self):
      return funcao.mostrador_de_codigo(self._linha, 142, 172)

   def mostrar_numero_local(self):
      return funcao.mostrador_de_codigo(self._linha, 172, 177)
      
   def mostrar_nome_cidade(self):
      return funcao.mostrador_de_codigo(self._linha, 192, 212)

   def mostra_cep(self):
      cep = funcao.mostrador_de_codigo(self._linha, 212, 220)
      return f"{cep[:5]}-{cep[5:]}"

   def mostrar_sigla_estado(self):
      return funcao.mostrador_de_codigo(self._linha, 220, 222)

   def __str__(self):
      return "|{}|{}          |{}|{}|{}             |".format(
         self.mostrar_logradouro(),
         self.mostrar_numero_local(),
         self.mostrar_nome_cidade(),
         self.mostra_cep(),
         self.mostrar_sigla_estado()
      )