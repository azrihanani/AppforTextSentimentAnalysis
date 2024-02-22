import streamlit as st
import sidebarpage
import textblob
page=sidebarpage.show()
import textblobalgo
if(page=="TextBlob Analysis"):
  textblobalgo.displayPage()
