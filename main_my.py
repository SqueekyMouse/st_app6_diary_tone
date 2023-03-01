import streamlit as st
import plotly.express as px
import glob
from pathlib import Path
from datetime import datetime
from nltk.sentiment import SentimentIntensityAnalyzer
# commit: Initial commit Sec35

st.title('Diary Tone')

filepaths=glob.glob('diary/*.txt')
filepaths=sorted(filepaths) #get filepaths sorted probably by date
analyzer=SentimentIntensityAnalyzer()

list_date=[]
list_pos_tone=[]
list_neg_tone=[]
for filepath in filepaths:
    ddate=datetime.strptime(Path(filepath).stem, '%Y-%m-%d').strftime('%b %d')
    list_date.append(ddate)
    with open(filepath) as file:
        diary=file.read()
        # print(analyzer.polarity_scores(diary))
        score=analyzer.polarity_scores(diary)
        list_pos_tone.append(score['pos'])
        list_neg_tone.append(score['neg'])

st.subheader('Positivity')
# chart
fig_pos=px.line(x=list_date,y=list_pos_tone,
                labels={'x':'Date','y':'Positivity'})
st.plotly_chart(fig_pos)

st.subheader('Negativity')
# chart
fig_neg=px.line(x=list_date,y=list_neg_tone,
                labels={'x':'Date','y':'Negativity'})
st.plotly_chart(fig_neg)

