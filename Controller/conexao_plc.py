    
class PLC:
    def __init__(self):
        pass

    ####### FUNÇÃO PARA CRIAR A CONEXÃO #######
    def Conexao(self,ip):
        try:         
            with PLC() as comm:
                comm.IPAddress = ip
                comm.Micro800 = True
                return comm
        except Exception as e:
            return False