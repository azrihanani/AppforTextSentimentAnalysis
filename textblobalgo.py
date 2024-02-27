from textblob import TextBlob
import streamlit as st
import streamlit.components.v1 as components
from PIP import Image
import tkinter as tk
from tkinter import font

#create user defined function
def displayPage():
  st.subheader("Text Analysis Using Textblob")
  st.text("Enter text to be analyzed")
  userText=st.text_input('Input',placeholder='Input text here')
  st.text(" ")
  if st.button('Predict'):
    if(userText!=""):
      st.componenets.v1.html("""<h3 style="color:#02C7C7;font.Font(family="Poppins", size=30;margin-bottom:8px;margin-top:40px;">RESULT</h3>""",height=150)
      getSentiment(userText)

#Write user defined function getsentiment
def getSentiment(userText):
  polarity,subj,status=getpolarity(userText)
  if(status=="Positive"):
    image=Image.open('./images/positive.png')
  elif(status=="Negative"):
    image=Image.open('./images/negative.png')
  else:
    image=Image.open('./images/neutral.png')

def getPolarity(userText):
tb=TextBlob(userText)
polarity=round(tb.polarity,2)
subj=round(tb.subjectivity,2)
  if polarity>0:
    return polarity,subj,"Positive"
  elif polarity==0:
    return polarity,subj,"Neutral"
  else:
    return polarity,subj,"Negative"
