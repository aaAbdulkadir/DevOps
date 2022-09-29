import streamlit as st
import pandas as pd
import geopandas
from matplotlib import pyplot as plt
import plotly.express as px
import numpy as np
import calendar

# title
st.markdown("# Galleria Holdings")
st.sidebar.markdown('# Galleria Holdings')
st.sidebar.subheader('Full project on [GitHub](https://github.com/aaAbdulkadir/DataPortfolio/tree/main/Bootcamp/Final%20Project)')


# caption
caption = '''
    An ETL pipeline which involves data warehousing for business analytical reporting.
'''
st.caption(caption)

overview, technologies, architectures, final_result = st.tabs(["Overview", "Technologies", "Architecture", "Final Result"])

with overview:
    overview_string = """
        This project started of with a brief from Galleria Holdings, a fast-food chain,
        who are looking to grow and improve their business. In order to achieve this, they
        require business intelligence reporting of their data through data warehousing. Hence, this project 
        consisted of creating a datawarehouse for business intelligence
        reporting. This consisted of creatubg an ETL pipeline whereby the data was provided,
        transformed and then put into a data warehouse. Finally, a dashboard with specific requirements was
        created for Galleria Holdings.
    """
    outcome_string = """
        From this project, I learnt how to create an OLAP Star Schema using SQL queries and 
        use PowerBI.
    """
    st.subheader('Outline')
    st.markdown(overview_string)
    st.subheader('Learning Outcome')
    st.markdown(outcome_string)
with technologies:
    st.subheader('Technologies Implemented')
    with st.expander("Python"):
        st.write('Used pandas for data wrangling, matplotlib and seaborn for visualisations.')
    with st.expander("Microsoft SQL"):
        st.write('Python data was imported into SQL and exported to PowerBI. Addtionally, a data warehouse was created using an OLAP Star Schema.')
    with st.expander("PowerBI"):
        st.write('Used to create the final dashboard for reporting.')
with architectures:
    st.subheader('Architectural Diagram')
    st.image('pages/galleria.png')
with final_result:
    st.write("""
    This data has been provided once by Galleria Holdings 
    for business intelligence reporting.
    """)

    st.subheader('Overview')

    sales = pd.read_csv('pages/data/galleria/sales.csv')

    no_customers = sales['TicketNo'].unique().shape[0]
    revenue = sales['Revenue'].sum()

    # metric cards
    col1, col2=  st.columns(2)

    col1.metric(label='Number of Customers', value=f"{no_customers:,}")
    col2.metric(label='Revenue', value=f"£{revenue:,}")

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


    outlet = pd.read_csv('pages/data/galleria/outlet.csv')

    st.write('''
    List of cities in which Galleria Holdings operate:
    ''')
    st.write(outlet['Outlet'].to_list())

    st.write('')
    st.write('')
    st.subheader('Popular Items')

    # -- order quantity and revenue -- #
    name = pd.read_csv('pages/data/galleria/name.csv')

    st.write("""
        The most important insight for Galleria Holdings is to see which
        items are the most popular and which items are generating the most revenue.
    """)

    st.write('')

    sales_name_merge = sales.merge(name, how='left', on='StockCode')
    
    order_quantity_pop = sales_name_merge.groupby('Name').agg({'Order Quantity':'sum'}).sort_values('Order Quantity', ascending=False).reset_index()
    revenue_pop = sales_name_merge.groupby('Name').agg({'Revenue':'sum'}).sort_values('Revenue', ascending=False).reset_index()

    def popular_barchart(data, feature):
        fig = px.bar(data, x='Name', y=feature)
        fig.update_layout(title={
            'text':f"Item vs {feature}",
            'y':.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
            xaxis=dict(
                range=[-0.5, 8.5])
        )
        return fig

    option = st.selectbox(
    'Select metric to view the most popular item by that category',
    ('Order Quantity', 'Revenue'))

    st.write('Note: Use the controls to zoom out or pan to see the whole dataset')

    if option == 'Order Quantity':
        st.plotly_chart(popular_barchart(order_quantity_pop, 'Order Quantity'))
    else:
        st.plotly_chart(popular_barchart(revenue_pop, 'Revenue'))
        


    st.subheader('Product Categories')

    st.write("""
        By looking at the products which are being bought the most as well
        as the products which are generating the most revenue, Galleria Holdings
        will be able to consolidate their menu and only sell products which are 
        successful.
    """)

    group = pd.read_csv('pages/data/galleria/group.csv')
    sales_group = sales.merge(group, how='left', on='ProductGroup')

    
    def product_piechart(data):
        fig = px.pie(data, values='Order Quantity', names='Group Name', color_discrete_sequence=px.colors.sequential.Plasma)
        fig.update_layout(title={
            'text':f"Most Popular Product Categories",
            'y':.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
        return fig

    st.plotly_chart(product_piechart(sales_group))

    def product_barchart(data):
        data = data.groupby('Group Name').agg({'Revenue':'sum'}).reset_index()
        data = data.sort_values('Revenue', ascending=False)
        fig = px.bar(data, x='Group Name', y='Revenue')
        fig.update_layout(title={
            'text':f"Products Categories Generating the Most Revenue",
            'y':.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
            xaxis=dict(
                range=[-0.5, 8.5])
        )
        return fig

    st.plotly_chart(product_barchart(sales_group))


    st.write('')
    st.subheader('Time of Year')

    st.write("""
        Galleria Holdings can look at their sales over the span of a year or even
        their life time to look at how their sales fluctuate throughout the year and
        try capitilise on specific times of the year or perhaps try to increase their
        sales in periods where the sales are not as high. Additionally, they can look
        at their performance over the years and see whether the company is progressing
        or regressing.
    """)

    sales['SaleDate'] = pd.to_datetime(sales['SaleDate'])
    sales['Month'] = pd.DatetimeIndex(sales['SaleDate']).month
    sales['Year'] = pd.DatetimeIndex(sales['SaleDate']).year
    
    def timeperiod(data, period):
        data = data.groupby(period).agg({'Order Quantity':'sum', 'Revenue':'sum'}).reset_index()
        
        # order quantity
        fig = px.line(
        data,
        x=period, 
        y='Order Quantity', 
        )
        fig.update_layout(title={
            'text':f"Order Quantity vs {period}",
            'y':.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
        if period == 'Month':
            fig.update_xaxes(
                tickmode = 'array',
                tickvals = data[period],
                ticktext= ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
            )
        else:
            fig.update_xaxes(
                tickmode = 'array',
                tickvals = data[period],
                ticktext= ['2016', '2017', '2018', '2019']
            )
        st.plotly_chart(fig)

        # revenue
        fig = px.line(
        data,
        x=period, 
        y='Revenue', 
        )
        fig.update_layout(
            title={
            'text':f"Revenue vs {period}",
            'y':.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
        if period == 'Month':
            fig.update_xaxes(
                tickmode = 'array',
                tickvals = data[period],
                ticktext= ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
            )
        else:
            fig.update_xaxes(
                tickmode = 'array',
                tickvals = data[period],
                ticktext= ['2016', '2017', '2018', '2019']
            )
        st.plotly_chart(fig)

    st.write('')
    option = st.selectbox(
    'Select time period',
    ('Month', 'Year'))

    if option == 'Month':
        timeperiod(sales, 'Month')
    else:
        timeperiod(sales, 'Year')

    st.subheader('Location')

    st.write("""
        Galleria Holdings can look at their outlets to see which outlets are 
        perfomring the best.
    """)

    location = sales.merge(outlet, how='left', on='OutletID')
    location = location.merge(name, how='left', on='StockCode')

    location['Month'] = pd.DatetimeIndex(location['SaleDate']).month
    location['Month'] = location['Month'].apply(lambda x: calendar.month_abbr[x])


    # monthly league table
    months = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
    option = st.selectbox(
    'Monthly league table', months)

    def location_by_month(data, month):
        data = data[data['Month'] == month]
        data = data.groupby('Outlet').agg({'Revenue':'sum'}).reset_index()
        data = data.sort_values('Revenue', ascending=False)
        fig = px.bar(data, x='Outlet', y='Revenue')
        fig.update_layout(title={
            'text':f"Revenue From Different Outlets",
            'y':.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
            xaxis=dict(
                range=[-0.5, 8.5])
        )
        return fig

    for month in months:
        if option == month:
            st.plotly_chart(location_by_month(location, month))
            

    # weekly league table
    weeks = [x for x in range(1,53)]
    option = st.selectbox(
    'Weekly league table', weeks)

    def location_by_week(data, week):
        data = data[data['WeekNo'] == week]
        data = data.groupby('Outlet').agg({'Revenue':'sum'}).reset_index()
        data = data.sort_values('Revenue', ascending=False)
        fig = px.bar(data, x='Outlet', y='Revenue')
        fig.update_layout(title={
            'text':f"Revenue From Different Outlets",
            'y':.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
            xaxis=dict(
                range=[-0.5, 8.5])
        )
        return fig

    for week in weeks:
        if option == week:
            st.plotly_chart(location_by_week(location, week))

    # product table for each outlet
    location = location[['Name', 'Outlet', 'Order Quantity', 'Revenue']]
    location = location.groupby(['Outlet', 'Name']).agg({'Order Quantity':'sum', 'Revenue':'sum'}).sort_values(['Outlet', 'Order Quantity'], ascending=[True, False]).reset_index()
    location = location.groupby('Outlet').head(3)

    outlet_names = ('Worthing', 
                    'Poole',
                    'Peterborough',
                    'London',
                    'Middlesborough',
                    'Birmingham',
                    'Weymouth',
                    'Edinburgh',
                    'Ipswich',
                    'Cardiff')

    option = st.selectbox(
    'Select location to see top three products in that location and the revenue generated',
    outlet_names)

    for outlet in outlet_names:
        if option == outlet:
            st.write(location[location['Outlet'] == outlet][['Name', 'Order Quantity', 'Revenue']])    
    