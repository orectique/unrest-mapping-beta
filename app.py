import streamlit as st
import plotly.express as px

import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/orectique/unrest-mapping-beta/main/Factors.csv')
upperYear = data['Year'].max()
lowerYear = data['Year'].min()

st.set_page_config(
    page_title= 'Unrest Evaluation Mapping',
    page_icon = '🌐',
)

body = st.container()

st.sidebar.title('Unrest Evaluation Mapping')
with st.sidebar.expander('About'):
    st.write('''This interactive graph is a rendition of a study which explored the creation
                            of a new mapping system to effectively capture the scale and hence enable the comparison of social unrest across countries
                            and years. Unrest Severity captures the fatality and peacefulness of protests in a country-year and Unrest Intensity represents the number of 
                            days of protest in a year. A high Unrest Severity value indicates that the events in the country-year were more violent than peaceful and saw a lot of fatalities
                            and a low Unrest Severity value implies that events in the country-year were more peaceful than violent and saw a relatively low number of fatilites.                            
                            To use the graph, choose countries from the dropdown menu and select the range of years using the slider below.''')

with st.sidebar.form('filters'):
    countries = st.multiselect('Select Countries', data['Country'].unique())
    lowYear, upYear = st.select_slider('Select Year Range', [i for i in range(lowerYear, upperYear+1)], (lowerYear, upperYear))

    submit = st.form_submit_button('Plot')


with body:
    if submit:
        
        if len(list(countries)) == 0:
            st.write('Please select at least one country')
            df0 = pd.DataFrame({"Unrest Severity":[], "Unrest Intensity": []})
            fig = px.scatter(df0, x="Unrest Severity", y="Unrest Intensity", title = "UEM Across Years")

        else: 
            df = data[data['Country'].isin(countries)]
            df = df[df['Year'].between(lowYear, upYear)]
            fig = px.scatter(df, x="Unrest Severity", y="Unrest Intensity", color = 'Country', hover_data=['Year'], title = "UEM Across Years")

        fig.update_xaxes(range=[-7, 7])
        fig.update_yaxes(range=[-2, 3.5])
    
        fig.update_layout(
    font_family="Times New Roman",
    title_font_family="Times New Roman")
        st.write(fig)