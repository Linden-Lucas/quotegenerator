import streamlit as st
from random import randint

quotes = []

st.title("WMG Quotes")

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

quiz = st.checkbox("Quizz mode")
st.markdown("----", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: grey;'>"+str(randQuote[0])+"</h1>", unsafe_allow_html=True)
if not quiz: 
    st.markdown("<h5 style='text-align: center; color: grey;'>"+str(randQuote[1])+"</h5>", unsafe_allow_html=True)
    st.markdown("", unsafe_allow_html=True)
    columns = st.columns((2, 1, 2))
    button_pressed = columns[1].button("Get new quote")
else:
    columns = st.columns((1,1,1,1,1))
    st.markdown("", unsafe_allow_html=True)
    
st.markdown("----", unsafe_allow_html=True)