import streamlit as st
from streamlit_option_menu import option_menu

def show():
  bg="""<div style='background-color:yellow'>
          <h1 style='color:white'>Sentiment Analysis</h1>
    </div>"""
  st.markdown(bg,unsafe_allow_html=True)
  with st.sidebar:
    selectedoption=option_menu(
      menu_title="Select the type of Machine Learning for Text Sentiment Analysis",
      options= ["TextBlob Analysis", "Text2Emotion Analysis", "VADER Sentiment Analysis"], #required
      default_index=0,)
    return selectedoption
