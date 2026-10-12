import streamlit as st

st.set_page_config(
    page_title="Crypto Analytics",
    page_icon=":chart_with_upwards_trend:"
)

pg = st.navigation([
    st.Page("pages/dashboard.py", title="Dashboard"),
    st.Page("pages/movimentacoes.py", title="Movimentações", default=True),
    st.Page("pages/mercado.py", title="Mercado")
])




