import pandas as pd
import streamlit as st
import plotly.express as px
from urllib.error import URLError

st.set_page_config(page_title = 'Intellia Dashbords lot4')
st.markdown("# Marche: 2 lot4")
st.sidebar.header(" Marche 2 lot4")
st.write(""" In this page we will plot just the figure and tables for the lots4""")

@st.cache
def get_data():
    df = pd.read_excel('C:/Users/PC74/PycharmProjects/StreamLite_Project/inte.xlsx')
    return df

df = pd.read_excel('C:/Users/PC74/PycharmProjects/StreamLite_Project/inte.xlsx')
Marche2 = ['KARIAT BA MED', 'MEKNES MENZAH', 'KENITRA', 'RABAT CENTRE ', 'RABAT RYAD', 'SALA ALJADIDA', 'SALA AL MADINA', 'SIDI SLIMANE', 'SKHIRAT HARHOURA']
#lots = df['lots'].unique().tolist()
#city = df['city'].unique().tolist()

try:
    df = get_data()
    city_selection2 = st.multiselect("Choose the city",
                          Marche2,
                          default=Marche2)

    mask = df['city'].isin(city_selection2)
    if not city_selection2:
        st.error("Please select at least one city.")
    else:
        # --- Display the table
        df_grouped = df[mask].groupby(by=['city']).sum()[['nbr_vue_max_jour', 'v_num', 'v_index', 'nbr_vue_min_jour']]
        st.table(df_grouped)

        # --- PLOT BAR CHART
        bar_chart = px.bar(df[mask],
                           x='city',
                           y='v_num',
                           text='v_index',
                           color_discrete_sequence=['#F63366'] * len(df_grouped),
                           template='plotly_white')
        st.plotly_chart(bar_chart)


        # --- Plot the Pie chart
        pie_chart = px.pie(df[mask], title='Total No Index vue',  values='v_index', names='city')
        st.plotly_chart(pie_chart)

except URLError as e:
    st.error(
        """
        **This demo requires internet access.**
        Connection error: %s
    """
        % e.reason
    )