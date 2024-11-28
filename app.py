import streamlit as st
from welcomePage import Welcome_page
from gamePage import Game_page
from statisticsPage import Stats_page

pages = [
    st.Page(Welcome_page, title="Welcome", default=True),
    st.Page(Game_page, title="Game"),
    st.Page(Stats_page, title = "Statistics")
    ]

pg = st.navigation(pages)

pg.run()


#https://aiandtheweb-theguessinggame.streamlit.app/