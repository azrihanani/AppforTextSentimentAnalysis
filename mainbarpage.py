import streamlit as st
import sidebarpage
import textblob
page=sidebarpage.show()
if(page=="TextBlob Analysis"):
  TextBlob.displayPage()
