import pandas as pd
import streamlit as st
import plotly.express as px
from urllib.error import URLError

st.set_page_config(page_title = 'Intellia Dashbords lot3')
st.markdown("# Marche: 1 lot3")
st.sidebar.header(" Marche 1 lot3")
st.write(""" In this page we will plot just the figure and tables for the lots3""")

@st.cache
def get_data():
    df = pd.read_excel('C:/Users/PC74/PycharmProjects/StreamLite_Project/inte.xlsx')
    return df

df = pd.read_excel('C:/Users/PC74/PycharmProjects/StreamLite_Project/inte.xlsx')
Marche1 = ['ALHOCEIMA',  'BERKANE', 'MEDIAQ', 'TANGER BENI MAKAD', 'TETOUAN', 'NADOR', 'OUJDA ANGAD', 'OUJDA VILLE', 'TAZA']
#lots = df['lots'].unique().tolist()
#city = df['city'].unique().tolist()

try:
    df = get_data()
    city_selection = st.multiselect("Choose the city",
                          Marche1,
                          default=Marche1)

    mask = df['city'].isin(city_selection)
    if not city_selection:
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