import streamlit as st
import pandas as pd
import geopandas
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib import pyplot as plt
import plotly.express as px
import numpy as np
import graphviz as graphviz

# title
st.markdown("# COVID-19")
st.sidebar.markdown("# COVID-19")
st.sidebar.subheader('Full project on [GitHub](https://github.com/aaAbdulkadir/DataPortfolio/tree/main/Exploratory%20Data%20Analysis/COVIDProject)')

# caption
caption = '''
    An automated ETL pipeline that collects COVID-19 data and transforms the data for analysis.
'''
st.caption(caption)

overview, technologies, architectures, final_result = st.tabs(["Overview", "Technologies", "Architecture", "Final Result"])

with overview:
    overview_string = """
        This project consisted of creating an ETL pipeline whereby 
        COVID data was collected from the World Data website and this data was
        transformed to creaet useful analytical insights for reporting on PowerBI 
        The dashboard was automated to update every day with the latest data and this 
        was done locally using windows task scheduler.
    """
    outcome_string = """
        From this project, I improved on my skills in data wrangling using pandas and
        data visualisation using matplotlib and seaborn. I also improved on my PowerBI skills.
    """
    st.subheader('Outline')
    st.markdown(overview_string)
    st.subheader('Learning Outcome')
    st.markdown(outcome_string)
with technologies:
    st.subheader('Technologies Implemented')
    with st.expander("Python"):
        st.write('Used selenium to extract the data, pandas for data wrangling, matplotlib and seaborn for visualisations.')
    with st.expander("Microsoft SQL"):
        st.write('Python data was imported into SQL and exported to PowerBI.')
    with st.expander("PowerBI"):
        st.write('Used to create the final dashboard for reporting.')

with architectures:
    st.subheader('Architectural Diagram')
    st.image('pages/covid.png')
    
with final_result:
    df = pd.read_csv('pages/data/covid/initial_df.csv')

    # --- date --- #
    
    df['date'] = pd.to_datetime(df['date'])
    date_formatted = df['date'].max()

    # day and month flipped
    day, month, year = date_formatted.month, date_formatted.day, date_formatted.year

    st.subheader(f"Snapshot of Data: {day}/{month}/{year}")

    st.write("""
        Note: this is only a snap shot of the data i.e. at one point in time as
        the automation script was turned off.
    """)

    st.write('')
    st.write('')

    # --- Total cases and deaths --- #
    m = pd.read_csv('pages/data/covid/m.csv')

    total_cases = m['new_cases'].sum()
    total_deaths = m['new_deaths'].sum()
    
    st.subheader('Overview')

    # metric
    col1, col2=  st.columns(2)

    col1.metric(label="Total Cases", value=f"{total_cases:,}")
    col2.metric(label="Total Deaths", value=f"{total_deaths:,}")

    st.markdown("""
        <style>
        div[data-testid="metric-container"] {
        background-color: rgba(28, 131, 225, 0.1);
        border: 1px solid rgba(28, 131, 225, 0.1);
        padding: 5% 5% 5% 10%;
        border-radius: 5px;
        color: rgb(30, 103, 119);
        overflow-wrap: break-word;
        }

        /* breakline for metric text         */
        div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
        overflow-wrap: break-word;
        white-space: break-spaces;
        color: White;
        }
        </style>
    """
    , unsafe_allow_html=True)

    # world map
    location = m[['iso_code', 'continent', 'location', 'new_cases', 'new_deaths']]

    # use geopandas to get locations --> refer to my github covid project for clarity
    world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

    world.at[21,'iso_a3'] = 'NOR'
    world.at[43,'iso_a3'] = 'FRA'
    world.at[174,'iso_a3'] = 'OWID_KOS'
    world.at[160,'iso_a3'] = 'OWID_CYN'

    merged = location.groupby(['iso_code', 'location']).sum().reset_index()
    merged = merged.rename(columns={'new_cases':'total_cases', 'new_deaths':'total_deaths'})
    merged_df = world.merge(merged, how='left', left_on=['iso_a3'], right_on=['iso_code'])
    merged_df = merged_df.set_index('name') # necessary for plotly

    st.write('')
    st.write('How are these cases and deaths distributed around the world?')
    st.write('')

    def map(feature):
        if feature == 'total_cases':
            colors = 'blues'
        else:
            colors = 'reds'
        fig = px.choropleth(merged_df, geojson=merged_df.geometry, 
                            locations=merged_df.index, color=f"{feature}",
                            height=350,
                        color_continuous_scale=colors)
        fig.update_geos(fitbounds="locations", visible=True)
        fig.update_layout(
            title_text=f"Total {feature.split('_')[-1]} in the world"
        )
        fig.update(layout = dict(title=dict(x=0.5)))
        fig.update_layout(
            margin={"r":0,"t":30,"l":10,"b":10},
            coloraxis_colorbar={
                'title':'Sum'},
            )
        return fig

    st.plotly_chart(map('total_cases'))
    st.plotly_chart(map('total_deaths')) 

    # -- global data -- #

    st.write('')
    st.write('')
    st.subheader('Global Statistics')

    a = pd.read_csv('pages/data/covid/a.csv')
    b = pd.read_csv('pages/data/covid/b.csv')
    c = pd.read_csv('pages/data/covid/c.csv')

    # pie chart
    def pie_chart(data, feature):
        title = feature.split('_')
        title = ' '.join(title)
        fig = px.pie(data, values=feature, names='location', title=f"Continental {title}")
        return fig

    # line graphs
    d = pd.read_csv('pages/data/covid/d.csv')
    d['date'] = pd.to_datetime(d['date'])
    d['date'] = d['date'].dt.strftime('%Y-%m-%D')

    def line_chart(feature):
        fig = px.line(
        d,
        x="date", 
        y=feature, 
        )
        fig.update_xaxes(nticks=10)
        y_axis = f"{feature.split('_')[-2]}"
        fig.update_layout(yaxis_title=y_axis,title={
            'text':f"{y_axis.title()} vs Time",
            'y':.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
        return fig
    

    option = st.selectbox(
    'How did COVID-19 spread across the globe? Select metric to view global data in that category',
    ('Cases', 'Deaths', 'Vaccinations'))

    if option == 'Cases':
        st.plotly_chart(pie_chart(a, 'total_cases_per_population'))
        st.plotly_chart(line_chart('new_cases_smoothed'))
    elif option == 'Deaths':
        st.plotly_chart(pie_chart(b, 'total_deaths_per_total_cases'))
        st.plotly_chart(line_chart('new_deaths_smoothed'))
    else:
        st.plotly_chart(pie_chart(c, 'people_vaccinated_per_population'))
        st.plotly_chart(line_chart('new_vaccinations_smoothed'))

    # -- Leading Stats -- #

    e = pd.read_csv('pages/data/covid/e.csv')
    f = pd.read_csv('pages/data/covid/f.csv')

    st.write('')
    st.write('')
    st.subheader('Leading Statistics')

    def bar_chart(data, feature):
        fig = px.bar(data, x='location', y=feature)
        title = feature.split('_')[1:]
        title = ' '.join(title)
        fig.update_layout(yaxis_title=title,title={
            'text':f"Total {title} vs Location",
            'y':.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
        return fig

    option = st.selectbox(
    'Which countries are affected the most for its population? Select metric to view leading data in that category',
    ('Cases', 'Deaths'))

    if option == 'Deaths':
        st.plotly_chart(bar_chart(e, 'total_deaths_per_population'))
    else:
        st.plotly_chart(bar_chart(f, 'total_cases_per_population'))


    # world vaccition chart
    st.subheader('Total Vaccination Status')

    st.write('How does the vaccination status vary across the globe?')

    i = pd.read_csv('pages/data/covid/i.csv')

    i = i.rename(columns={'people_fully_vaccinated':'Full Vaccination', 'people_vaccinated': 'Vaccination','population':'Population'})

    fig = px.histogram(i, x='location', y=[i['Full Vaccination'], i['Vaccination'], i['Population']],
             barmode='group',
             histfunc='avg',
             height=400)

    fig.update_layout(yaxis_title='', xaxis_title='Location', title={
            'text':"Difference in vaccinations across the continents",
            'y':.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
        
    st.plotly_chart(fig)



    # vaccination pie chart
    st.write('')
    st.write('')

    g = pd.read_csv('pages/data/covid/g.csv')
    h = pd.read_csv('pages/data/covid/h.csv')


    def vaccination_piechart(data):

        def split(string):
            if '_' in string:
                string = string.split('_')
                return ' '.join(string).title()
            else:
                return string.title()

        data['index'] = data['index'].apply(split)
        fig = px.pie(data, values='value', names='index', color_discrete_sequence=px.colors.sequential.Greens_r)
        return fig

    option = st.selectbox(
    'What is the vaccination percentage in the world? Select metric to view vaccination data',
    ('Fully vs Partial Vaccination', 'Population Vaccination'))

    if option == 'Fully vs Partial Vaccination':
        st.plotly_chart(vaccination_piechart(g))
    else:
        st.plotly_chart(vaccination_piechart(h))


    # -- Annual Statistics -- #

    st.write('')
    st.write('')
    
    st.subheader('Annual Statistics')

    st.write('')
    j = pd.read_csv('pages/data/covid/j.csv')
    k = pd.read_csv('pages/data/covid/k.csv')
    l = pd.read_csv('pages/data/covid/l.csv')

    option = st.selectbox(
    'Select metric to view annual data in that category',
    ('Cases', 'Deaths', 'Vaccinations'))

    def annual_barchart(data, feature):
        fig = px.bar(data, x='year', y=feature)
        title = feature.split('_')[1:]
        title = ' '.join(title).title()
        fig.update_layout(yaxis_title=title.title(), xaxis_title='Year',title={
            'text':f"Total {title} vs Year",
            'y':.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
        return fig


    if option == 'Cases':
        st.plotly_chart(annual_barchart(j, 'new_cases'))
    elif option == 'Deaths':
        st.plotly_chart(annual_barchart(k, 'new_deaths'))
    else:
        st.plotly_chart(annual_barchart(l, 'new_people_vaccinated_smoothed'))




    






