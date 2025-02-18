from pylogix import PLC


class Acionamento_Saida_PLC:
    def __init__(self, ):
        pass

    def AcionarSaida(self, conexao,saida):
        self.conexao = conexao
        self.conexao.Write(saida, value=True)
        print(f"Acionando a saída {saida}")
        #Read(Variareislogicas,8).Value
        
    def DesligarSaida(self, conexao,saida):
        self.conexao = conexao
        self.conexao.Write(saida, value=False)
        print(f"Desligando a saída {saida}")
        #Read(Variareislogicas,8).Value