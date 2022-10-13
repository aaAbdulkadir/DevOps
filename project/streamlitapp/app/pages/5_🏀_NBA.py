import streamlit as st
import pandas as pd

# title
st.markdown("# NBA")
st.sidebar.markdown("# NBA")
st.sidebar.subheader("""Full projects on GitHub - [Classification](https://github.com/aaAbdulkadir/DataPortfolio/blob/main/ML%20Projects/NBA%20Classification.ipynb) and [Regression](https://github.com/aaAbdulkadir/DataPortfolio/blob/main/ML%20Projects/NBA%20MVP%20Prediction%20Regression.ipynb) """)


# caption
caption = '''
    MAchine leanring classification and regression of NBA data.
'''
st.caption(caption)

overview, technologies, architectures, results = st.tabs(["Overview", "Technologies", "Architecture", "Final Results"])

with overview:
    overview_string = """
        For this project, two machine learning models were created using NBA datasets, one being 
        regression, and the other, classification. The regression model consisted of prediciting 
        who would win the MVP award at the end of this current season using player performance statistics and this worked by predicting the MVP
        win share, which is a number that corresponds to a share of how many votes a player gets. 
        This was calculated using regression and then sorted to find the top voted. The classification model
        consisted of determining the position of a player based on their statistics. The project is explained thoroughly in
        their notebooks.
    """
    outcome_string = """
        From these projects, I learnt how to train and a test a machine 
        laerning model, and with that, make predictions for both regression and 
        classification. With the regression model, I learnt how to use the RMSE with cross 
        validation to evaluate the perforamnce of a regression model and compare them with
        eachother to find the best models. With that, I went onto use grid search for these
        top models to tune the models for an optimal regressor. Likewise, with classfication, I 
        compared the classification report i.e. precision, recall and F1-score using cross validation and
        again, used grid search to find the optimal classifier.


    """
    st.subheader('Outline')
    st.markdown(overview_string)
    st.subheader('Learning Outcome')
    st.markdown(outcome_string)
with technologies:
    st.subheader('Technologies Implemented')
    with st.expander("Python"):
        st.write("""
        Used pandas for data wrangling, matplotlib and seaborn 
        for visualisations, scikit-learn for machine learning 
        and beautifulsoup for data collection.
        """)
with architectures:
    st.subheader('Architectural Diagram')
    st.image('pages/nba.png')

with results:

    st.subheader('Regression')

    st.caption('''Prediction of MVP winner each year, but to predict the 2
    022 winner. The data ranges from 1987 to 2022. The accuracy with the combination of
    two models is .72, where both models had a mean RMSE of less than 0.002 of the
    predictions.
    ''')

    reg = pd.read_csv('pages/data/nba/regression.csv', index_col=[0])
    reg = reg.rename(columns={'Rk':'Rank',
                            'Final_Predicted_Rk':'Predicted Rank',
                            'Final_Predicted_Winner':'Predicted Winner'
                            })
    st.write(reg)

    st.subheader('Classification')

    st.caption('''Prediction of position of a player playing in the 2022 season. 0, 1 and 2 corresponds to
    the positions 0:[PG], 1:[SG, SF], 2:[PF, C].
    The data ranges from 1987 to 2022. The precision, recall and f1-score is .77, .76, .76
    ''')

    classif = pd.read_csv('pages/data/nba/classification.csv', index_col=[0])
    classif = classif.rename(columns={'prediction':'Prediction'})
    st.write(classif)
