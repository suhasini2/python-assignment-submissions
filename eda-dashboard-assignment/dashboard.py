import requests
import pandas as pd
import plotly.express as px
import streamlit as st

res=requests.get("https://jsonplaceholder.typicode.com/posts")

data=res.json()

df=pd.DataFrame(data)
df=df.rename(columns={'userId': 'user_id'})
df=df.drop('id',axis=1)

post_count=df.groupby("user_id").size().reset_index(name='post_count')

df['post_length'] = df['body'].apply(len)

print(df.head())

st.subheader("Dashboard")
st.write("1. Dataset Preview")
st.dataframe(df)

st.write("2. Posts per User")
fig_bar=px.bar(post_count,x='user_id',y='post_count',title="Users vs Posts",labels={'body':'Posts', 'user_id':"users"})
st.plotly_chart(fig_bar)

st.write("3. Post Length Distribution")
fig_hist= px.histogram(df,x="post_length", nbins=10,title="Post Length",labels={'title_length':"Characters per post"})
st.plotly_chart(fig_hist)