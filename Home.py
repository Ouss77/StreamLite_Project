import streamlit as st
st.set_page_config(
    page_title="Hello Intellia",
    page_icon="👋")

st.sidebar.title('Navigation')
#uploaded_file = st.sidebar.file_uploader('Upload your file here')
#st.sidebar.radio('pages', options=['data statistics', 'data science'])
#choice = st.sidebar.selectbox("Les marches", ["Marche1", "Marche2", "Marche3"])



st.header('Dashboards and Graphs')
st.subheader('The app will be split depending on the lots that exists')
st.write("# Welcome to Intellia ! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects."""
)