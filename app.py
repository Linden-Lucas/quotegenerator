import streamlit as st
from random import randint

quotes = []

with open("quotes.txt", "r") as file:
    quotes = [line.strip().split("|") for line in file]

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-color: red;
}}
[data-testid="stHeader"] {{
visibility: hidden;
}}
[class*="st-emotion-cache"]{{display: none;}}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

try:
    tempQuotes = st.session_state.quotes
except:
    tempQuotes = quotes

if tempQuotes == []:
    tempQuotes = quotes

randIndex = randint(0,len(tempQuotes)-1)
randQuote = tempQuotes[randIndex]
tempQuotes.pop(randIndex)
st.session_state.quotes = tempQuotes

st.markdown("----", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: grey;'>"+str(randQuote[0])+"</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: grey;'>"+str(randQuote[1])+"</h5>", unsafe_allow_html=True)
st.markdown("", unsafe_allow_html=True)
columns = st.columns((2, 1, 2))
button_pressed = columns[1].button("Get new quote")
st.markdown("----", unsafe_allow_html=True)
