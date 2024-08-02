print('my dashboard.janani')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.write('my dashboard.janani')
# text
st.title('Variablz Acadamy')
st.header('Training Institute')
st.subheader('Data Analyst Program')
st.caption('Variablz Acadamy')
st.text('Learning')
# dataframe
data = 'data/cars.csv'

df = pd.read_csv(data)

st.dataframe(df, width=1000, height=400)
# matplotlib
fig = plt.figure(figsize=(10,4))
ax = fig.add_subplot()
ax.scatter(df['Displacement'], df['Horsepower'])
st.write(fig)

# seaborn
df = pd.read_csv('data/cars.csv')

fig = plt.figure(figsize=(10,4))
ax = fig.add_subplot()
ax=sns.heatmap(
    df.corr(numeric_only=True), cmap='vlag', annot=True)
st.write(fig)

# side bar
with st.sidebar:
    st.subheader('Sidebar')

st.header('Main Dashboard')

# columns
cols = st.columns(3)

with cols[0]:
    st.header('column1')

with cols[1]:
    st.header('column2')

with cols[2]:
    st.header('column3')

# Tabs
app_tabs = ['Employees', 'Students']
tabs = st.tabs(app_tabs)

with tabs[0]:
    st.header('Employees')
with tabs[1]:
    st.header('Students')

# Expander
with st.expander('Setting:'):
    st.write('Choose Your Theme')
   

st.header('Main Dashboard')

# Buttons
def greetings():
    st.write('Welcome to Variablz')

btn_welcome = st.button(label='Welcome', on_click=greetings)

# Check Box
agree = st.checkbox('I agree for Terms & Conditions')

if agree:
    st.write('User agreed, create account')
else:
    st.write('User declined, cancel operation')

# Radiobutton
gender = st.radio(label = 'Select gender', 
                  options=
                   ['Female', 'Male']
)
if gender == 'Female':
    st.write("Welcome Ma'am")
else:
    st.write("Welcome Sir")

# Select box
country= st.selectbox(label = 'Choose country', 
             options = ['India', 'London', 'Japan', 'China']
)

st.write(f'User from {country}')

# Multi Select box
course = st.multiselect(label = 'Choose Course',
            options = ['Python', 'SQL', 'Java', 'Matplotlib']

)
st.write(f'User from {course}')

# File upload
data = st.file_uploader(label = 'Choose CSV File', type='csv')
if data:
    df = pd.read_csv(data)
    st.DataFrame(data=df)

with st.sidebar:
    st.subheader('cars.csv')



# Dowload Files
ravi = ['Ravi', 25, 'Design Engineer', 'Milacron']
ragul = ['Ragul',26, 'FEA Engineer', 'Mold Masters']
rocky = ['Rocky', 29, 'Senior engineer', 'LMW']
friends = [ravi, ragul, rocky]

df = pd.DataFrame(friends)
df.columns = ['Name', 'Age', 'Job Title', 'Company']

st.download_button(
    label ='Download Data', 
    data = df.to_csv(),
    file_name ='friends.csv'
)