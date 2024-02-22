import streamlit as st
import sidebarpage
import textblobalgo
page=sidebarpage.show()
ifpage=="TextBlob Analysis":
     textblobalgo.displayPage()

