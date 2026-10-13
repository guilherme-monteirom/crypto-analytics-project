import streamlit as st
from datetime import date
import psycopg2
from dotenv import load_dotenv
import os

st.markdown("""
<style>
.block-container {
    padding-top: 1rem;
    padding-bottom: 2rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown("# Operações do Portfólio")

st.write("""
Registre compras e vendas para acompanhar sua carteira.

### Nova Operação
""")

with st.form("form_operacao"):

    # Tipo de operação e ativo
    col1, col2 = st.columns(2)

    with col1:
        selected_operation = st.selectbox(
            "Tipo:",
            ["Compra", "Venda"],
        )

    with col2:
        selected_ticker = st.selectbox(
            "Ticker:",
            ["BTC", "ETH", "SOL", "XRP", "ADA", "BNB"]
        )

    # Quantidade e preço
    col3, col4 = st.columns(2)

    with col3:
        quantidade = st.number_input(
            "Quantidade:",
            min_value=0.0,
            value=0.0,
            step=0.001,
            format="%.8f"
        )

    with col4:
        preco_unitario = st.number_input(
            "Preço unitário (R$):",
            min_value=0.0,
            value=0.0,
            step=0.01,
            format="%.2f"
        )

    # Data e corretora
    col5, col6 = st.columns(2)

    with col5:
        data_operacao = st.date_input(
            "Data da operação:",
            value=date.today(),
            format="DD/MM/YYYY"
        )

    with col6:
        corretora = st.selectbox(
            "Corretora:",
            ["Binance", "Bybit", "Coinbase", "Mercado Bitcoin", "Outra"]
        )

    # Observação
    observacao = st.text_area(
        "Observação:",
        placeholder="Adicione detalhes da operação (opcional)",
        height=10
    )

    # Envio do formulário
    submitted = st.form_submit_button(
        "Registrar operação",
        type="primary"
    )

if submitted:
    valor_total = quantidade * preco_unitario

    if quantidade <= 0 or preco_unitario <= 0:
        st.error("Informe uma quantidade e um preço maiores que zero.")
    else:

        load_dotenv()
        user = os.getenv("user")
        password = os.getenv("password")
        port = os.getenv("port")

        query = f"""
        INSERT INTO tb_movimentacoes (
            tipo, ticker, quantidade, preco_unitario, data_operacao, corretora, observacao)
        VALUES (
            %s, %s, %s, %s, %s, %s, %s)"""
        
        try:
            conexao = psycopg2.connect(
                host= "localhost",
                database= "crypto_analytics",
                user= user,
                password= password,
                port= port
            )
            print("Conectado com sucesso!")

            with conexao.cursor() as cursor:
                cursor.execute(query,
                (
                    selected_operation,
                    selected_ticker,
                    quantidade,
                    preco_unitario,
                    data_operacao,
                    corretora,
                    observacao
                )
            )
            print("Carga concluída")

            conexao.commit()
            cursor.close()
            conexao.close()
        
            st.success("Operação registrada com sucesso!")

            st.write("### Resumo da operação")
            st.write(f"**Tipo:** {selected_operation}")
            st.write(f"**Ativo:** {selected_ticker}")
            st.write(f"**Quantidade:** {quantidade}")
            st.write(f"**Preço unitário:** R$ {preco_unitario:,.2f}")
            st.write(f"**Valor total:** R$ {valor_total:,.2f}")
            st.write(f"**Data:** {data_operacao.strftime('%d/%m/%Y')}")
            st.write(f"**Corretora:** {corretora}")
            st.write(f"**Observação:** {observacao or 'Nenhuma'}")

        except Exception as e:
            print(repr(e))

            cursor.close()
            conexao.close()
            
            st.error("Falha no registro da operação, tente novamente mais tarde!")