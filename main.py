import streamlit as st
from Controller.conexao_plc import PLC_Rockwell
from Controller.acionamento_saida import Acionamento_Saida_PLC


def Main():
    plc_conect = PLC_Rockwell()
    acionamento = Acionamento_Saida_PLC()
    lista_saidas = ["saida0","saida1","saida2","saida3","saida4","saida5","saida6","saida7",
                    "saida8","saida9","saida10","saida11","saida12","saida13",
                    "saida14","saida15","saida16","saida17","saida18","saida19"]
    st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="collapsed", menu_items=None)
    st.text("Controlador CLP - Micro 820 e Micro 850 - Python")
    st.divider()
    with st.container(height=100):
        coluna1,coluna2,coluna3,coluna4 = st.columns([2,1.1,1.4,10],vertical_alignment='bottom')
        result_ip = coluna1.text_input("Insira o IP do CLP")
        btn_conectar = coluna2.button("Conectar")
        btn_desconectar = coluna3.button("Desconectar")

    if btn_conectar:
        result_ip = str(result_ip)
        if result_ip == "":
            st.error("Insira o IP do CLP")
        else:
            resul_conect = plc_conect.Conexao(result_ip)
            if resul_conect != False:
                st.session_state['conexao'] =  resul_conect
                print(st.session_state['conexao'])
                st.success("Conectado com sucesso")
            else:
                st.error("Erro ao conectar")


    if btn_desconectar:
        statsus_conect = plc_conect.Desconectar(st.session_state['conexao'])
        if statsus_conect == True:
            st.success("PLC Desconectado com sucesso")

    coluna6,coluna7,coluna8,coluna9 = st.columns([4,4,4,0.5])

    coluna6.text("Acionamento das Saídas")
    saida = coluna6.selectbox("Selecione a Saída",["saida0","saida1","saida2","saida3","saida4","saida5","saida6","saida7",
                                                   "saida8","saida9","saida10","saida11","saida12","saida13",
                                                   "saida14","saida15","saida16","saida17","saida18","saida19"])
    btn_ligar_saida = coluna6.button("Ligar Saida")

    if btn_ligar_saida:
        if st.session_state['conexao'] != True:
            st.error("Conecte ao CLP")
        else:
            print(st.session_state['conexao'],saida)
            acionamento.AcionarSaida(st.session_state['conexao'],saida)

    btn_desligar_saida = coluna6.button("Desligar Saida")
    if btn_desligar_saida:
        if st.session_state['conexao'] != True:
            st.error("Conecte ao CLP")
        else:
            print(st.session_state['conexao'],saida)
            acionamento.DesligarSaida(st.session_state['conexao'],saida)
    st.divider()

    with st.container(height=300):
        coluna11,coluna15 = st.columns([8,1])
        coluna11.text("Estado das Saídas")
        coluna11.table({"Saída":["saida0","saida1","saida2","saida3","saida4","saida5","saida6","saida7","saida8",'saida9','saida10','saida11',
                                 'saida12','saida13','saida14','saida15','saida16','saida17','saida18','saida19'],
                        "Estado":["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]})

if __name__ == "__main__":
    Main()
