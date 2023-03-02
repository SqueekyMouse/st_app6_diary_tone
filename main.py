import streamlit as st
import plotly.express as px
import glob
from pathlib import Path
# from datetime import datetime
from nltk.sentiment import SentimentIntensityAnalyzer
# commit: debug: print sentiment score Sec35

st.title('Diary Tone')

filepaths=sorted(glob.glob('diary/*.txt'))
analyzer=SentimentIntensityAnalyzer()

list_date=[file.strip('.txt').strip('diary/') for file in filepaths] # no need to format date as plotly will parse date itself!!!
# list_date=[datetime.strptime(Path(filepath).stem, '%Y-%m-%d').strftime('%b %d') for filepath in filepaths]

list_pos_tone=[]
list_neg_tone=[]
for filepath in filepaths:
    with open(filepath) as file:
        diary=file.read()
    score=analyzer.polarity_scores(diary)
    # print(score)
    list_pos_tone.append(score['pos'])
    list_neg_tone.append(score['neg'])

st.subheader('Positivity')
fig_pos=px.line(x=list_date,y=list_pos_tone,
                labels={'x':'Date','y':'Positivity'})
st.plotly_chart(fig_pos)

st.subheader('Negativity')
fig_neg=px.line(x=list_date,y=list_neg_tone,
                labels={'x':'Date','y':'Negativity'})
st.plotly_chart(fig_neg)

