import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
st.sidebar.title('Navigation')
uploaded_file = st.sidebar.file_uploader('Upload your file here')
st.sidebar.radio('pages', options=['data statistics', 'data science'])
choice = st.sidebar.selectbox("Les marches", ["Marche1", "Marche2", "Marche3"])


### --- LOAD DATAFRAME
excel_file = 'inte.xlsx'
df = pd.read_excel(excel_file)

#df_participants.dropna(inplace=True)

# --- STREAMLIT SELECTION
lots = df['lots'].unique().tolist()
city = df['city'].unique().tolist()
Marche1 = ['ALHOCEIMA', 'MEDIAQ', 'TANGER_BENI_MAKAD' ,'TETOUAN', 'BERKANE', 'NADOR', 'OUJDA_ANGAD', 'OUJDA_VILLE', 'TAZA']

department_selection = st.multiselect('Marche1:',
                                    Marche1,
                                    default=Marche1)

lots_selection = st.slider('lots:',
                        min_value= min(lots),
                        max_value= max(lots),
                        value=(min(lots),max(lots)))

city_selection = st.multiselect('City:',
                                    city,
                                    default=city)

# --- FILTER DATAFRAME BASED ON SELECTION
st.date_input("pick a date")

mask1 = df['city'].isin(department_selection)

mask = (df['lots'].between(*lots_selection)) & (df['city'].isin(city_selection))
number_of_result = df[mask].shape[0]
st.markdown(f'*Available Results: {number_of_result}*')

df_grouped = df[mask].groupby(by=['lots']).sum()[['v_num']]
df_grouped = df_grouped.reset_index()

# --- PLOT BAR CHART
bar_chart = px.bar(df_grouped,
                   x='lots',
                   y='v_num',
                   text='lots',
                   color_discrete_sequence = ['#F63366']*len(df_grouped),
                   template= 'plotly_white')
st.plotly_chart(bar_chart)

# print the table
df_grouped1 = df[mask1].groupby(by=['city']).sum()[['nbr_vue_max_jour','v_num', 'v_index',  'nbr_vue_min_jour']]
st.table(df_grouped1)

# --- PLOT PIE CHART
pie_chart = px.pie(df,
                title='Total No Index vue',
                values='v_index',
                names='lots')

st.plotly_chart(pie_chart)

if __name__ == '__main__':
    main()