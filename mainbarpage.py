import streamlit as st
import sidebarpage
import textblob
page=sidebarpage.show()
if page=="TextBlob Analysis":
     from textblobalgo import display_page
     
     display_page()
