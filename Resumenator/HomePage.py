import streamlit as st
#from streamlit_option_menu import option_menu
from jinja2 import Environment, FileSystemLoader, select_autoescape
from Resume import temp1
from Portfolio import temp2
import base64  # Import the base64 module
if 'resume1' not in st.session_state:
        st.session_state['resume1']=True
if 'temp1' not in st.session_state:
    st.session_state['temp1']=False
if 'temp2' not in st.session_state:
    st.session_state['temp2']=False
st.sidebar.header("Select your Templates")

st.sidebar.image("Portfolio.png",caption="Portfolio",use_column_width=True)
temp_button2 = st.sidebar.button("Portfolio 💼", key='btn2')


st.write("\n\n")

st.sidebar.image("Resume.jpeg",caption="Resume",use_column_width=True)
temp_button1 = st.sidebar.button("Resume 📁",key="btn1")

image_options = {
    "Template 1": "/Users/mitta/OneDrive/Pictures/Screenshots/template1.png",
    "Template 2": "/Users/mitta/OneDrive/Pictures/Screenshots/template1.png"
}
    #st.sidebar.image("/Users/mitta/OneDrive/Pictures/Screenshots/template1.png",caption="Template 1",use_column_width=True)
    #st.sidebar.image("/Users/mitta/OneDrive/Pictures/Screenshots/template2.png",caption="Template 2",use_column_width=True)
if temp_button1 and not st.session_state['temp1']:
    st.session_state['temp1']=True
    st.session_state['temp2']=False
    temp1()
elif temp_button2 and not st.session_state['temp2']:
    st.session_state['temp2']=True
    st.session_state['temp1']=False
    temp2()
elif st.session_state['temp1']:
    temp1()
elif st.session_state['temp2']:
    temp2()
