from msilib import type_short
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import datetime as dt

st.set_page_config(layout="wide")
st.markdown('<div style="text-align: center;font-size:60px;font-weight:bold;">Tantangan Cyber Attack di Era Digital</div>', unsafe_allow_html=True)

st.markdown('<div style="text-align: justify;font-size:40px;">Cyber attack adalah ................\
    </div>', unsafe_allow_html=True)

df = pd.read_csv("patrolisiber.csv")
df.astype({col: int for col in df.columns[1:]})
#df['Bulan'] = pd.to_datetime(df['Bulan'].apply(lambda x: dt.datetime.strptime(x, '%b-%y')))
#df['Bulan'] = df['Bulan'].dt.to_period('M')

type_s = df[['Bulan', 'Child_Porn', 'Criminal', 'Hoax', 'Pemalsuan_Dokumen', 'Pemerasan', 'Pengancaman', 'Penghinaan_Pencemaran', 'Penistaan_Agama', 'Penjualan_narkoba_illegal_di_internet', \
        'Perdagangan_Hewan_yang_Dilindungi', 'Perdagangan_Orang', 'Perjudian', 'Provokasi_Penghasutan']].set_index(['Bulan'])       
# type_s['Bulan'].value_counts(sort=False).reindex(
#     pd.Series(pd.date_range("1-Jan-2020", freq="M", periods=12)).dt.strftime("%B")
# ) 
tab1, cht1 = st.columns([1, 4])
with tab1:
    st.write(df, height= 500)
with cht1:
    st.bar_chart(type_s, height= 500)