import streamlit as st
from random import randint

quotes = []

st.set_page_config(page_title="WMG Quotes")

with open("quotes.txt", "r") as file:
    quotes = [line.strip().split("|") for line in file]

t = []
for elem in quotes:
    t.append(elem[1])
teachers = set(t)

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
st.session_state.numberCorrect = 0
st.session_state.numberWrong = 0

def option1Varify():
    if correct == 0:
        st.session_state.correct = True
        st.session_state.numberCorrect += 1
        return
    st.session_state.correct = False
    st.session_state.numberWrong += 1

def option2Varify():
    if correct == 1:
        st.session_state.correct = True
        st.session_state.numberCorrect += 1
        return
    st.session_state.correct = False
    st.session_state.numberWrong += 1

def option3Varify():
    if correct == 2:
        st.session_state.correct = True
        st.session_state.numberCorrect += 1
        return
    st.session_state.correct = False
    st.session_state.numberWrong += 1

topBar = st.columns((1,1,1))
quiz = topBar[0].checkbox("Quizz mode")
topBar[1].write("Correct: "+str(st.session_state.numberCorrect))
topBar[2].write("Wrong: "+str(st.session_state.numberWrong))
st.markdown("----", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: grey;'>"+str(randQuote[0])+"</h1>", unsafe_allow_html=True)
if not quiz: 
    st.markdown("<h5 style='text-align: center; color: grey;'>"+str(randQuote[1])+"</h5>", unsafe_allow_html=True)
    st.markdown("", unsafe_allow_html=True)
    columns = st.columns((2, 1, 2))
    button_pressed = columns[1].button("Get new quote")
if quiz:
    st.write("hi")
    correct = -1
    columns = st.columns((1,1,1,1,1))
    st.markdown("", unsafe_allow_html=True)
    tempTeachers = list(teachers)
    i = randint(0,len(tempTeachers)-1)
    teacher1 = tempTeachers[i]
    tempTeachers.pop(i)
    i = randint(0,len(tempTeachers)-1)
    teacher2 = tempTeachers[i]
    tempTeachers.pop(i)
    i = randint(0,len(tempTeachers)-1)
    teacher3 = tempTeachers[i]
    tempTeachers.pop(i)
    match randint(0,2):
        case 0:
            teacher1 = randQuote[1]
            correct = 0
        case 1:
            teacher2 = randQuote[1]
            correct = 1
        case 2:
            teacher3 = randQuote[1]
            correct = 2
    option1 = columns[0].button(teacher1,on_click=option1Varify)
    option2 = columns[1].button(teacher2,on_click=option2Varify)
    option3 = columns[2].button(teacher3,on_click=option3Varify)
st.markdown("----", unsafe_allow_html=True)
try:
    if st.session_state.correct:
        st.title("Correct!")
    else:
        st.title("Incorrect!")
except:
    st.write("")