import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import nsepython as nse
import plotly.express as px


# Set header
st.header("Significant Level Finder - Equity")

# Get index list
stock_list = nse.nse_eq_symbols()


# Set initial inputs
script = st.selectbox('Select Index',stock_list,index=0)
st.write("Select data window ")
col11,col12 = st.columns(2)
start_date = col11.date_input("From").strftime(format="%d-%m-%Y")
end_date = col12.date_input("To").strftime(format="%d-%m-%Y")

# Get data downloaded
df = nse.equity_history(symbol=script,
                      series = "EQ",
                       start_date = start_date,
                       end_date=end_date
                       )

st.write(df)

# Clean data
df = df[['CH_TIMESTAMP','CH_TRADE_HIGH_PRICE','CH_TRADE_LOW_PRICE',
    'CH_OPENING_PRICE','CH_CLOSING_PRICE']] # select columns
df.columns = ['Date','Open','Low','High','Close'] # change column names
# Datatype transformation
df['Date'] = pd.to_datetime(df['Date'])
df['Close'] = df['Close'].astype(float)
df['High'] = df['High'].astype(float)
df['Low'] = df['Low'].astype(float)
df['Open'] = df['Open'].astype(float)

df = df.set_index('Date') # Set index
# df['CloseOpenAvg'] = round((df['Close']+df['Open'])/2,2) # Feature addition


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
              step=2,
              help = text)

if (df.max().max() > 0) & (df.max().max() <= 1000):
    data = (df[target]//10*10).value_counts()
elif (df.max().max() > 1000) & (df.max().max() <= 5000):
    data = (df[target]//20*20).value_counts()
elif (df.max().max() > 5000) & (df.max().max() <= 10000):
    data = (df[target]//50*50).value_counts()
else:
    data = (df[target]//100*100).value_counts()

data = df[target].value_counts()
data = data[data>n]
levels = list(data.keys())
strength = list(data.values)

df = df.sort_index(ascending=True)
fig = px.line(x=df[target].index,y=df[target]) 
for i,j in zip(levels,strength):
    fig.add_hline(i)
st.plotly_chart(fig)

