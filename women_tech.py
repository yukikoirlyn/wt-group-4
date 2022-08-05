import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import datetime as dt
import altair as alt
import plotly.express as px

st.set_page_config(layout="wide")
st.markdown('<div style="text-align: center;font-size:60px;font-weight:bold;">Tantangan Cyber Attack di Era Digital</div>', unsafe_allow_html=True)

st.markdown('<div style="text-align: justify;font-size:40px;">Cyber attack adalah ................\
    </div>', unsafe_allow_html=True)

df = pd.read_csv("patrolisiber.csv")
df.astype({col: int for col in df.columns[1:]})

type_s = df[['Bulan', 'Child_Porn', 'Criminal', 'Hoax', 'Pemalsuan_Dokumen', 'Pemerasan', 'Pengancaman', 'Penghinaan_Pencemaran', 'Penistaan_Agama', 'Penjualan_narkoba_illegal_di_internet', \
        'Perdagangan_Hewan_yang_Dilindungi', 'Perdagangan_Orang', 'Perjudian', 'Provokasi_Penghasutan']].set_index(['Bulan'])       
 
dfl_unpivot = pd.melt(df, id_vars='Bulan', value_vars=['Child_Porn', 'Criminal', 'Hoax', 'Pemalsuan_Dokumen', 'Pemerasan', 'Pengancaman', 'Penghinaan_Pencemaran', 'Penistaan_Agama', 'Penjualan_narkoba_illegal_di_internet', \
        'Perdagangan_Hewan_yang_Dilindungi', 'Perdagangan_Orang', 'Perjudian', 'Provokasi_Penghasutan'])

lap = px.bar(dfl_unpivot, x = "Bulan", y = "value", color = "variable")
lap.update_layout(xaxis_type='category')
tab1, cht1 = st.columns([1, 4])
with tab1:
    st.write(df, height= 500)
with cht1:
    st.plotly_chart(lap, use_container_width=True)
