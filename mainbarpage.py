import streamlit as st
import sidebarpage
import textblob
import textblobalgo
page=sidebarpage.show()
if(page=="TextBlob Analysis"):
  textblobalgo.displayPage()
