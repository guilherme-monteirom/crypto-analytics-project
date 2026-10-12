import streamlit as st

st.set_page_config(
    page_title="Crypto Analytics",
    page_icon=":chart_with_upwards_trend:"
)

pg = st.navigation([
    st.Page("pages/main_page.py", title="Dashboard"),
    st.Page("pages/page_2.py", title="Movimentações", default=True),
    st.Page("pages/page_3.py", title="Mercado")
])




