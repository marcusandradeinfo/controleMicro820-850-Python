from pylogix import PLC
import time


class LerSaidas:
    def __init__(self):
        self.saidas = ['False','False','False','False','False',
                       'False','False','False','False','False',
                       'False','False','False','False','False',
                       'False','False','False','False','False']

    def LerSaidas(self, conexao):
        self.conexao = conexao
        for i in range(20):
            time.sleep(0.1)
            self.saidas[i] = (self.conexao.Read(f"saida{i}").Value)
