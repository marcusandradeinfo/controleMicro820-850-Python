import streamlit as st

def Main():
    st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="collapsed", menu_items=None)
    st.text("Controlador CLP - Micro 820 e Micro 850 - Python")
    st.divider()
    with st.container(height=100):
        coluna1,coluna2,coluna3,coluna4 = st.columns([2,2,2,8],vertical_alignment='bottom')
        result_ip = coluna1.text_input("Insira o IP do CLP")
        btn_conectar = coluna2.button("Conectar")
        btn_desconectar = coluna3.button("Desconectar")
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
if __name__ == "__main__":
    Main()
