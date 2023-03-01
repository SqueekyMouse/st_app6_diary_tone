import streamlit as st
import plotly.express as px
import glob
# commit: Initial commit Sec35

st.title('Diary Tone')

st.subheader('Positivity')

# chart
fig_pos=px.line(x=[],y=[],labels={'x':'Date','y':'Positivity'})
st.plotly_chart(fig_pos)

st.subheader('Negativity')

# chart
fig_neg=px.line(x=[],y=[],labels={'x':'Date','y':'Negativity'})

