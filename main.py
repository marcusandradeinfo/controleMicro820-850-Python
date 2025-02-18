import streamlit as st
from Controller.conexao_plc import PLC

def Main():
    plc_conect = PLC()
    st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="collapsed", menu_items=None)
    st.text("Controlador CLP - Micro 820 e Micro 850 - Python")
    st.divider()
    with st.container(height=100):
        coluna1,coluna2,coluna3,coluna4 = st.columns([2,1.1,1.4,10],vertical_alignment='bottom')
        result_ip = coluna1.text_input("Insira o IP do CLP")
        btn_conectar = coluna2.button("Conectar")
        btn_desconectar = coluna3.button("Desconectar")

    if btn_conectar:
        resul_conect = plc_conect.Conexao(result_ip)
        if resul_conect:
            st.success("Conectado com sucesso")
        else:
            st.error("Erro ao conectar")

    coluna6,coluna7,coluna8,coluna9 = st.columns([4,4,4,0.5])

    coluna6.text("Acionamento das Entradas")
    entrada = coluna6.selectbox("Selecione a Entrada",["I:0/0","I:0/1","I:0/2","I:0/3","I:0/4","I:0/5","I:0/6","I:0/7"])
    btn_ligar_entrada = coluna6.button("Ligar Entrada")
    btn_desligar_entrada = coluna6.button("Desligar Entrada")



    coluna8.text("Acionamento das Saídas")
    saida = coluna8.selectbox("Selecione a Saída",["O:0/0","O:0/1","O:0/2","O:0/3","O:0/4","O:0/5","O:0/6","O:0/7"])
    btn_ligar_saida = coluna8.button("Ligar Saida")
    btn_desligar_saida = coluna8.button("Desligar Saida")
    st.divider()

    with st.container(height=300):
        coluna10,coluna11 = st.columns([1,1])
        coluna10.text("Estado das Entradas")
        coluna11.text("Estado das Saídas")
        coluna10.table({"Entrada":["I:0/0","I:0/1","I:0/2","I:0/3","I:0/4","I:0/5","I:0/6","I:0/7"],
                        "Estado":["0","0","0","0","0","0","0","0"]})
        coluna11.table({"Saída":["O:0/0","O:0/1","O:0/2","O:0/3","O:0/4","O:0/5","O:0/6","O:0/7"],
                        "Estado":["0","0","0","0","0","0","0","0"]})
        

if __name__ == "__main__":
    Main()
