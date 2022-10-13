import streamlit as st
import graphviz as graphviz
import pandas as pd
import plotly.express as px

# title
st.markdown("# CoinMarketCap")
st.sidebar.markdown("# CoinMarketCap")
st.sidebar.subheader('Full project on [GitHub](https://github.com/aaAbdulkadir/DataPortfolio/tree/main/ZoomCamp/Project)')

# caption
caption = '''
    An automated ETL pipeline which transfers data from CoinMarketCap to Azure. 
'''
st.caption(caption)

# main
overview, technologies, architectures, final_result = st.tabs(["Overview", "Technologies", "Architecture", "Final Result"])

with overview:
    overview_string = """
        This project consisted of working with batch data to create a dashboard 
        for monitoring crypto currencies on a daily basis. 
        The data was collected from CoinMarketCap (a crypto currency website) 
        and transformed to produce useful datasets and charts to create a visual
        dashboard for daily monitoring.
    """
    outcome_string = """
        From this project and the learning process to get to the point in which I was
        able to do this project, I learnt some new skills. Firsly, I learnt what Terraform
        was and how to write Infrastructure as Code using Terraform for Azure. Then, I learnt
        how to use Docker containers by firsly starting off with learning how to create 
        a PostgresSQL database with its GUI, pgAdmin. With that, I also learnt how to ingest
        data into this database that was on a Docker container and the whole idea of port forwading.
        Moreover, I learnt how to use Apache Airflwo for pipeline creations and how to 
        run that on Docker. I had the opporunity to also develop my skills in Apache Spark. Finally,
        I became more comfortable using Azure as the project revolved around it. I learnt how 
        to use Azure Synapse Analytics, create SQL and Spark pools, data lakes and much more.
    """
    st.subheader('Outline')
    st.markdown(overview_string)
    st.subheader('Learning Outcome')
    st.markdown(outcome_string)

with technologies:
    st.subheader('Technologies Implemented')

    with st.expander("Terraform"):
        st.write("Created the Azure infrastructure using code. This consisted of creating a resource group, storage accoumt, a blob container, a virtual machine and everything that comes with it.")

    with st.expander('Azure'):
        st.write('Used Azure to store the data and run a virtual machine to host the pipeline on Docker.')

    with st.expander('Docker'):
        st.write('Hosted Airflow via docker-compose and all the dependencies needed for Spark and Python via Dockerfile.')
    
    with st.expander('Apache Airflow'):
        st.write('Created a pipeline that governed the process of moving the data.')

    with st.expander('Apache Spark'):
        st.write('Transformed the raw data into useful datasets.')

    with st.expander('PowerBI'):
        st.write('Visualised the data via a dashboard.')

with architectures:
    st.subheader('Architectural Diagram')

    st.image('pages/cmc.png')

    st.text("")
    st.text("")
    st.text("")

    st.subheader('Flow Chart')
    graph = graphviz.Digraph()
    st.graphviz_chart('''
        digraph {
            Terraform -> Azure -> VM
            VM -> Docker
            Docker -> Spark
            Spark -> Airflow
            Docker -> Airflow
            Airflow -> CoinMarketCap
            CoinMarketCap -> Airflow
            Airflow -> AzureBlobStorage
            AzureBlobStorage -> PowerBI
        }
    ''')


with final_result:

    # --- data collection ---

    # load data
    date = pd.read_csv('pages/data/cmc/Date.csv')

    date = date.rename(columns={'Earliest last_updated':'date_collected'})
    date['date_collected'] = pd.to_datetime(date['date_collected'])
    date_formatted = date['date_collected'][0]
    day, month, year = date_formatted.day, date_formatted.month, date_formatted.year
    st.subheader(f"Snapshot of Data: {day}/{month}/{year}")

    st.write("""
        Note: this is only a snap shot of the data i.e. at one point in time as
        the automation script was turned off.
    """)

    st.write('')
    st.write('')

    # -- performance of these top coins ---
    st.subheader(f"Performance of Top Crypto")

    st.write("""
        An important metric to monitor is the top cryptocurrency coins as their performance
        are an indication to the rest of the market. The following coins are top coins which 
        also are coins of interest...
    """)


    # load data
    performance = pd.read_csv('pages/data/cmc/fluctuations.csv')
    
    # 24 hour performance
    performance_24h = performance[performance['Time Frame'] == '24h']

    # get price
    summary = pd.read_csv('pages/data/cmc/pricechart.csv')
    summary = summary[summary['Coin'].isin(performance_24h['Coin'])]

    # merge tables
    summarised = summary.merge(performance_24h, how='left')

    # card formation
    def cards(coin):
        df = summarised[summarised['Coin'] == coin].reset_index(drop=True)
        return df['Coin'][0], df['Price'][0], df['Percentage Change'][0]

    st.write('')
    col1, col2, col3 = st.columns(3)

    col1.metric(label='Coin', value='Price', delta='Daily Change')
    col3.metric(label=cards('Ethereum')[0], value=cards('Ethereum')[1], delta=cards('Ethereum')[2])
    col2.metric(label=cards('Bitcoin')[0], value=cards('Bitcoin')[1], delta=cards('Bitcoin')[2])

    col1, col2, col3 = st.columns(3)
    col3.metric(label=cards('XRP')[0], value=cards('XRP')[1], delta=cards('XRP')[2])
    col1.metric(label=cards('BNB')[0], value=cards('BNB')[1], delta=cards('BNB')[2])
    col2.metric(label=cards('Cardano')[0], value=cards('Cardano')[1], delta=cards('Cardano')[2])

    st.write('')

    coins_of_interest = performance[performance['Coin'].isin(['Bitcoin', 'Ethereum', 'BNB', 'Cardano'])]
    
    st.write('')
    st.write('')  

    # centre chart with columns
    fig = px.line(
            coins_of_interest,
            x="Time Frame", 
            y="Percentage Change", 
            color="Coin",
            line_group="Coin", 
        )
    fig.update_layout(title_text='Percentage Change vs Time Frame', title_x=0.5)
    st.plotly_chart(fig)


    # --- Top performing coins in the last 90 days --- #
    st.subheader(f"90 Days Performance")
    st.write("""
        Another interesting way at looking at how well a project is performing
        is by looking at how they have been perfomring over the last 90 days.
    """)
    

    performance_90d = pd.read_csv('pages/data/cmc/best90days.csv')
    
    fig = px.line(
            performance_90d.head(10),
            x="Coin", 
            y="90D %", 
            width=665,
            height=450
        )
    fig.update_layout(title_text='Top 90 Days Performing Coins', title_x=0.5)
    st.plotly_chart(fig)


    # --- Top gainers, losers and trending --- #
    st.subheader('Top Gainers, Losers and Trending')
    st.write("""
        This sections shows which coins are performing the best and the in the last 24 hours
        as well as the coins which people are searching for.
    """)

    gainers = pd.read_csv('pages/data/cmc/gainers.csv')
    losers = pd.read_csv('pages/data/cmc/losers.csv')
    trending = pd.read_csv('pages/data/cmc/bs4trending.csv')

    gainers = gainers[['Coin', '24H %']].shift()[1:].head(10) # shift fixes index
    losers = losers[['Coin', '24H %']].shift()[1:].head(10)
    trending = trending[['Coin']].shift()[1:].head(10)
     
    left, middle, right = st.columns(3)
    with left:
        st.write('Top Gainers')
        st.dataframe(gainers)
    with middle:
        st.write('Top Losers')
        st.dataframe(losers)
    with right:
        st.write('Trending')
        st.write(trending)

    # -- User can filter -- #

    st.write('')
    st.write('')
    st.subheader('Monitor Your Own Coins')


    price_chart = pd.read_csv('pages/data/cmc/pricechart.csv')
    ranked = pd.read_csv('pages/data/cmc/ranked.csv')

    chart = price_chart.merge(ranked, how='left', left_on=['symbol', 'Coin'], right_on=['symbol', 'name'])
    chart = chart[['Coin', 'Price', 'Market Cap']]

    # select coins
    left, middle, right = st.columns((100, 1, 1))
    with left:
        coin_selection = st.multiselect(
            'Pick your cryptocurrency coins:',
            chart['Coin'])


    if len(coin_selection) < 1:
        st.subheader('Overview')
        st.write(chart)
    else:
        selected = chart[chart['Coin'].isin(coin_selection)]
        st.subheader('Overview')
        st.write(selected)
    
        st.write('')
        st.write('')
        # percentage changes
        st.subheader('Performance')
        selected_with_percentage = selected.merge(performance, how='left', on=['Coin'])
        fig = px.line(
                selected_with_percentage,
                x="Time Frame", 
                y="Percentage Change", 
                color="Coin",
                line_group="Coin", 
            )
        fig.update_layout(title_text='Percentage Change vs Time Frame', title_x=0.5)
        st.plotly_chart(fig)


    




    