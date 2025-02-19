from pylogix import PLC

class PLC_Rockwell:
    def __init__(self):
        pass

    ####### FUNÇÃO PARA CRIAR A CONEXÃO #######
    def Conexao(self,ip):
        with PLC() as comm:
            comm.IPAddress = ip
            comm.Micro800 = True
            print(comm)
            conexao = comm.Read("saida0").Value
            print(f'Print conexao: {conexao}')
            if conexao != None:
                return comm
            else:
                return False
            
    def Desconectar(self,conexao):
        conexao.Close()
        print("Desconectado com sucesso")
        return True