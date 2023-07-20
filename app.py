import streamlit as st
from fpdf import FPDF

# Função para calcular o subtotal para cada produto
def calcular_subtotal(quantidades, dicionario_produtos):
    subtotais = {}
    for produto, preco in dicionario_produtos.items():
        if produto in quantidades and quantidades[produto] > 0:
            subtotais[produto] = quantidades[produto] * preco
    return subtotais

# Função para gerar o PDF da nota fiscal
def gerar_pdf(quantidades, subtotais, total):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="TicTacToy - Nota Fiscal", ln=True, align="C")
    pdf.cell(200, 10, txt="==================================", ln=True, align="C")
    
    for produto, quantidade in quantidades.items():
        if quantidade > 0:
            preco_unitario = dicionario_produtos[produto]
            subtotal = subtotais[produto]
            pdf.cell(0, 10, txt=f"{produto} x{quantidade} - R${preco_unitario:.2f} (Subtotal: R${subtotal:.2f})", ln=True, align="L")

    pdf.cell(200, 10, txt="==================================", ln=True, align="C")
    pdf.cell(0, 10, txt=f"Total da compra: R${total:.2f}", ln=True, align="R")

    pdf.output("nota_fiscal.pdf")

# Configurações iniciais
st.set_page_config(page_title='TicTacToy - Gerar Nota Fiscal')
st.title('TicTacToy - Gerar Nota Fiscal')

dicionario_produtos = {'Caneta Carimbo Roller': 6.50, 'Marca texto duas pontas neon': 4.00, 'Caneta em gel colorida': 3.00, 'Marca texto com glitter': 5.00, 'Marca texto apagável': 6.50, 'Canetinha com carimbo': 6.00, 'Marca texto com ponta estrela': 5.00, 'Marca texto com ponta carimbo': 5.00, 'Marca texto bonecas 5 cores': 15.00, 'Marca texto polvo 5 cores': 15.00, 'Marca texto sorvete 5 cores': 15.00, 'Marca texto coração 6 cores': 17.00, 'Carimbos fofos': 3.00, 'Tesoura escolar': 6.00, 'Caderno Popit colorido': 35.00, 'Caderno Popit dino': 5.00, 'Marmita com borrachas de frutas 5 unidades': 20.00, 'Borracha batata frita 8 unidades': 25.00, 'Borracha chicken 8 unidades': 25.00, 'Borracha pão de forma': 4.50, 'Borracha macarron': 4.50, 'Apontador e borracha de fruta': 6.00, 'Fita corretiva 16m': 7.00, 'Cola dupla face em fita': 12.00, 'Caneta apagável astronauta': 6.00, 'Caneta com spray': 3.00, 'Caneta gel coração': 5.00, 'Caneta gel astronauta': 5.00, 'Caneta gel stitch': 5.00, 'Caneta gel cacto': 5.00, 'Caneta gel coelho': 5.00, 'Caneta gel Super Mario': 5.00, 'Caneta gel heróis': 5.00, 'Caneta gel Mickey e Minnie': 5.00, 'Caneta gel seringa': 5.00, 'Caneta gel sereia': 5.00, 'Caneta diamante': 8.00, 'Caneta mágica apagável': 8.00, 'Caderneta sereia luxo': 20.00, 'Diário astronauta': 30.00, 'Planner semanal gatinhos': 20.00, 'Planner semanal patinhas': 20.00, 'Clips cactos 6 unidades': 10.00, 'Clips diamantes 6 unidades': 10.00, 'Clips gatinhos 6 unidades': 10.00, 'Clips coração 6 unidades': 10.00, 'Jogo tabuada da multiplicação em madeira': 40.00, 'Jogo numerais e geometria em madeira': 40.00, 'Quebra-cabeça madeira ônibus': 20.00, 'Quebra-cabeça madeira alimentos': 35.00, 'Quebra-cabeça madeira dino': 20.00, 'Estojo de pintura carros': 15.00, 'Jogo UNO': 10.00, 'Canetinha magnética para lousa': 2.00, 'Refil caneta gel': 1.50}

# Interface do Streamlit
quantidades = {}
for produto in dicionario_produtos.keys():
    quantidades[produto] = st.number_input(f"Quantidade de {produto}", value=0, min_value=0, step=1)

if st.button("Gerar Nota Fiscal"):
    subtotais = calcular_subtotal(quantidades, dicionario_produtos)
    total = sum(subtotais.values())
    gerar_pdf(quantidades, subtotais, total)
    st.success("Nota fiscal gerada com sucesso! Clique no link abaixo para baixar o PDF.")
    st.markdown("[Baixar Nota Fiscal](nota_fiscal.pdf)")