import streamlit as st

pages = [
    st.pages(page="pages/pages01.py", titlle="home", icon="🏡"),
    st.pages(page="pages/pages02.py", titlle="home", icon="📊"),
    st.pages(page="pages/pages03.py", titlle="home", icon="⚙️")
]

pg = st.navigation(
    pages,
    position="sidebar",
    expanden= True
)

pg.run()