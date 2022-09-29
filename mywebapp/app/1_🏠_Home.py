import streamlit as st

st.set_page_config(
    page_title="Abdulkadir Portfolio WebApp",
    layout="centered",
    initial_sidebar_state="expanded",
)

# title
st.title('Welcome to My Portfolio WebApp!')
st.write(":heavy_minus_sign:" * 32)

with st.sidebar:
    st.markdown("# Home")

st.markdown("""

## Summary

Hi my name is Abdulkadir and I am an aspiring Data Engineer. Over the last 
year, I was discovering my career path. I knew I wanted to be in technology but it 
was just a matter of finding out what was appealing to me. A year ago, I started
working as a data analyst and this is what sparked my interest in data. At that point 
I was already programming and after six months, I felt like the job was not satisfying 
the capacity of what I can do. So I left and started doing projects in data, utilising 
everything that I had learnt. Purely from curiosity, I started asking myself how I would
solve certain problem and from this stemmed my learning of data science and data engineering.
From then until now, I have been doing various projects and I wanted to show case some of 
these projects all in one place, hence, why I learnt Streamlit. Therefore, you fill 
some of the projects that I have done on this portfolio web application.


## About me
- Self taught data science/analyst/engineer looking to break into data engineering.
- Data analysis experience.
- MEng Mechanical Engineering Graduate 2021.

## Skills
These are some of the skills I have acquired over the past year...
""")

st.json({
    'Python': [
        'Pandas',
        'Numpy',
        'Matplotlib',
        'Seaborn',
        'Scikit-Learn',
        'Beautifulsoup',
        'Selenium',
        'Streamlit'
    ],
    'SQL':['TSQL', 'Data Warehousing'],
    'Data Visualisation': ['PowerBI', 'Tableau'],
    'Azure Fundamentals': ['AZ-900', 'Synapse Analytics', 'Storage', 'Virtual Machines'],
    'IaC':'Terraform',
    'Containers': 'Docker',
    'CLI':['Linux','Git'],
    'Apache':['Spark', 'Airflow']})

st.markdown('## Looking to Learn')


st.write(['Kubernetes', 'CI/CD', 'Kafka'])

st.write('And learn more in eveyrthing that I have started learnt or started learning.')