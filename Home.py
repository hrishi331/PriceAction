import streamlit as st 

st.set_page_config("Significance Level Finder")

st.header("Siginificant Levels Finder")


text_1 = """
This gives you significant levels on selected index chart for selected time frame.
By adjusting significance you can get levels from low to high significance.
You can select parameter of your choice from OLHC.  
"""
st.write(text_1)
if st.button(label='For Indices >>'):
    st.switch_page(page='pages/1_Index.py')


text_2 = """
This gives you significant levels on selected equity chart for selected time frame.
By adjusting significance you can get levels from low to high significance.
You can select parameter of your choice from OLHC.  
"""
st.write(text_2)
if st.button(label='For Equity >>'):
    st.switch_page(page='pages/2_Equity.py')


text_3 = """
Feel free to contact us! 
"""
st.write(text_3)
if st.button(label='Contact Us >>'):
    st.switch_page(page='pages/3_ContactUs.py')
