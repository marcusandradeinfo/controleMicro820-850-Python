from pylogix import PLC

class LerSaidas:
    def __init__(self):
        self.saidas = []

    def LerSaidas(self, conexao):
        self.conexao = conexao
        for i in range(20):
            self.saidas.append(self.conexao.Read(f"saida{i}").Value)