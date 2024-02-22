import streamlit as st
import sidebarpage
import textblobalgo.py
page=sidebarpage.show()
if(page=="TextBlob Analysis"):
  textblobalgo.displayPage()
