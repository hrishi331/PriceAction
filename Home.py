import streamlit as st 

st.set_page_config("Significance Level Finder")

st.header("Siginificant Levels Finder")

st.page_link("pages/1_Index.py",label="**Index**")
text_1 = """
This gives you significant levels on selected index chart for selected time frame.
By adjusting significance you can get levels from low to high significance.
You can select parameter of your choice from OLHC.  
"""
st.write(text_1)

st.page_link("pages/2_Equity.py",label="**Equity**")
text_2 = """
This gives you significant levels on selected equity chart for selected time frame.
By adjusting significance you can get levels from low to high significance.
You can select parameter of your choice from OLHC.  
"""
st.write(text_2)

st.page_link("pages/3_ContactUs.py",label = "**Contact Us**")
text_3 = """
Feel free to contact us! 
"""
st.write(text_3)