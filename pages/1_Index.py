import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import nsepython as nse
import plotly.express as px


# Set header
st.header("Significant Level Finder - Index")

# Get index list
indices = nse.nse_get_index_list()

# Set initial inputs
script = st.selectbox('Select Index',indices,index=0)
st.write("Select data window ")
col11,col12 = st.columns(2)
start_date = str(col11.date_input("From"))
end_date = str(col12.date_input("To"))

# Get data downloaded
df = nse.index_history(symbol=script,
                       start_date = start_date,
                       end_date=end_date)

# Clean data
df = df[['HistoricalDate','OPEN','LOW','HIGH','CLOSE']] # select columns
df.columns = ['Date','Open','Low','High','Close'] # change column names

# Datatype transformation
df['Date'] = pd.to_datetime(df['Date'])
df['Close'] = df['Close'].astype(float)
df['High'] = df['High'].astype(float)
df['Low'] = df['Low'].astype(float)
df['Open'] = df['Open'].astype(float)

df = df.set_index('Date') # Set index
df['CloseOpenAvg'] = round((df['Close']+df['Open'])/2,2) # Feature addition

# rounding to nearest 50
# for i in df:
#     df[i] = df[i]//100*100  

df = df.sort_index(ascending=True)

st.subheader("RESULT")

target = st.radio("OLHC parameter",horizontal=True,options=['Close','Open','Low','High'])

text = f"""For smaller data window select lower values to get significant levels.
           For larger data window select higher values to get significant levels.
           If you don't see any levels in selected dataframe then either increase data window
           or select lower value."""
n = st.slider(label="Significance",
              min_value=2,
              max_value=100,
              step=1,
              help = text)


data = (df[target]//50*50).value_counts()
data = data[data>n]
levels = list(data.keys())
strength = list(data.values)

df = df.sort_index(ascending=True)
fig = px.line(x=df[target].index,y=df[target])
for i,j in zip(levels,strength):
    fig.add_hline(i)
st.plotly_chart(fig)