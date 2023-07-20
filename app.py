import streamlit as st
import datetime

# Função para calcular o subtotal para cada produto
def calcular_subtotal(quantidades, dicionario_produtos):
    subtotais = {}
    for produto, preco in dicionario_produtos.items():
        if produto in quantidades and quantidades[produto] > 0:
            subtotais[produto] = quantidades[produto] * preco
    return subtotais

# Função para mostrar a nota fiscal
def mostrar_tela(quantidades, subtotais, total):
    
    st.write("TicTacToy - Nota de Compras")
    st.write("============================================")
    
    for produto, quantidade in quantidades.items():
        if quantidade > 0:
            preco_unitario = dicionario_produtos[produto]
            subtotal = subtotais[produto]
            st.write(f"{produto} x{quantidade} - {preco_unitario:.2f} reais cada (Subtotal: {subtotal:.2f} reais)")

    st.write("============================================")
    st.write(f"Total da compra: R${total:.2f}")

    data_e_hora_atuais = datetime.now()
    diferenca = datetime.timedelta(hours=-3)
    fuso_horario = datetime.timezone(diferenca)
    data_e_hora_brasilia = data_e_hora_atuais.astimezone(fuso_horario)
    data_e_hora_brasilia_em_texto = data_e_hora_brasilia.strftime("%d/%m/%Y %H:%M")

    st.write(f"Data/Hora: {data_e_hora_brasilia_em_texto}")

# Configurações iniciais
st.set_page_config(page_title='TicTacToy - Gerar Nota de Compras')
st.title('TicTacToy - Gerar Nota de Compras')

dicionario_produtos = {'Caneta Carimbo Roller': 6.50, 'Marca texto duas pontas neon': 4.00, 'Caneta em gel colorida': 3.00, 'Marca texto com glitter': 5.00, 'Marca texto apagável': 6.50, 'Canetinha com carimbo': 6.00, 'Marca texto com ponta estrela': 5.00, 'Marca texto com ponta carimbo': 5.00, 'Marca texto bonecas 5 cores': 15.00, 'Marca texto polvo 5 cores': 15.00, 'Marca texto sorvete 5 cores': 15.00, 'Marca texto coração 6 cores': 17.00, 'Carimbos fofos': 3.00, 'Tesoura escolar': 6.00, 'Caderno Popit colorido': 35.00, 'Caderno Popit dino': 5.00, 'Marmita com borrachas de frutas 5 unidades': 20.00, 'Borracha batata frita 8 unidades': 25.00, 'Borracha chicken 8 unidades': 25.00, 'Borracha pão de forma': 4.50, 'Borracha macarron': 4.50, 'Apontador e borracha de fruta': 6.00, 'Fita corretiva 16m': 7.00, 'Cola dupla face em fita': 12.00, 'Caneta apagável astronauta': 6.00, 'Caneta com spray': 3.00, 'Caneta gel coração': 5.00, 'Caneta gel astronauta': 5.00, 'Caneta gel stitch': 5.00, 'Caneta gel cacto': 5.00, 'Caneta gel coelho': 5.00, 'Caneta gel Super Mario': 5.00, 'Caneta gel heróis': 5.00, 'Caneta gel Mickey e Minnie': 5.00, 'Caneta gel seringa': 5.00, 'Caneta gel sereia': 5.00, 'Caneta diamante': 8.00, 'Caneta mágica apagável': 8.00, 'Caderneta sereia luxo': 20.00, 'Diário astronauta': 30.00, 'Planner semanal gatinhos': 20.00, 'Planner semanal patinhas': 20.00, 'Clips cactos 6 unidades': 10.00, 'Clips diamantes 6 unidades': 10.00, 'Clips gatinhos 6 unidades': 10.00, 'Clips coração 6 unidades': 10.00, 'Jogo tabuada da multiplicação em madeira': 40.00, 'Jogo numerais e geometria em madeira': 40.00, 'Quebra-cabeça madeira ônibus': 20.00, 'Quebra-cabeça madeira alimentos': 35.00, 'Quebra-cabeça madeira dino': 20.00, 'Estojo de pintura carros': 15.00, 'Jogo UNO': 10.00, 'Canetinha magnética para lousa': 2.00, 'Refil caneta gel': 1.50}

# Interface do Streamlit
quantidades = {}
for produto in dicionario_produtos.keys():
    quantidades[produto] = st.number_input(f"Quantidade de {produto}", value=0, min_value=0, step=1)

if st.button("Gerar Nota de Compras"):
    subtotais = calcular_subtotal(quantidades, dicionario_produtos)
    total = sum(subtotais.values())
    mostrar_tela(quantidades, subtotais, total)
