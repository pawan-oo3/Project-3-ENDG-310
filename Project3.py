#ENDG 310 PROJECT 3
#SUBMITTED BY: Pawan Nihure, Khadiza Ahsan , Abdul Mohammed
import streamlit as st 
import pandas as pd
from streamlit_option_menu import option_menu
import time 
import matplotlib.pyplot as plt                                      #importing all the necessary in-built functions
from PIL import Image
import requests
from io import BytesIO
import plotly_express as px
import mpld3
import streamlit.components.v1 as components


st.set_page_config(page_title = 'ENDG 310 Project 3',page_icon =':computer:',layout = 'wide') #setup a webpage with page tutke and icon
df = pd.read_csv('atlcrime.csv',usecols=[1,2,3,6]) #read the csv file with the dataset
df['date'] = pd.to_datetime(df.date, format = "%m/%d/%Y") #create a new data set with ordered dates in particular format

def about_us():
    '''function to create the About Us page in the website. Uses Get Requests to strip images of the creators from the internet'''
    response1 = requests.get('https://english.onlinekhabar.com/wp-content/uploads/2021/05/ppawan-2.jpg')       #uses Get Requests to import image diretcly from the internet
    response2 = requests.get('https://www.ucalgary.ca/sites/default/files/styles/ucws_profiles_profile_picture/public/2022-07/Khadiza%20Binte%20Ahsan.jpg?h=afb6ea7c&itok=tm1Hcl-m')
    response3 = requests.get('https://assets.stickpng.com/images/585e4bf3cb11b227491c339a.png')
    image1 = Image.open(BytesIO(response1.content))   #opens the image
    st.subheader('Pawan Nihure')
    st.image(image1, caption = None, width = 200)     #displays image on the website
    st.write('Bachelors of Science in Biomedical Engineering, Minor in Digital Engineering')
    st.subheader('Khadiza Binte Ahasan')
    image2 = Image.open(BytesIO(response2.content))#opens the image
    st.image(image2, caption =None, width = 200 )      #displays image on the website
    st.write('Bachelors of Science in Biomedical Engineering, Minor in Digital Engineering')
    st.subheader('Abdul Rahem Mohammad')
    image3 = Image.open(BytesIO(response3.content))#opens the image
    st.image(image3, caption =None, width = 200 )       #displays image on the website
    st.write('Bachelors of Science in Biomedical Engineering, Minor in Digital Engineering')

def plot1():
    '''Function to display average no. of crimes vs Neighborhood as a Bar Graph. Also annotates the top 3 neighborhood with highest crime number
     and provie a user interactive plot interface for zooming in/out , supports manual graph movements with the cursor'''
    fig=plt.figure()
    neigh_list = df['neighborhood'].unique()
    c_neigh = df['number'].groupby(df['neighborhood']).mean()      # calculates the crime average for a particular neighborhood
    c_neigh.plot(x='neighborhood',y='number',kind='bar',figsize=(20,5),color='r') #plots the bar graph
    plt.annotate('Mellwood', xy =(146,7400000000),xytext =(146,7400000000))
                                  
    plt.annotate('Huntington', xy =(120,330000000),xytext =(120,3100000000))      #annotates the top 3 Highest Bars
                                  
    plt.annotate('Ben Hill Pines', xy =(27,450000000),xytext =(27,4300000000))
    plt.xticks(fontsize=4)
    plt.xlabel('Neighborhood',color='Purple')   #assigns x-label to the plot
    plt.ylabel('Number of Crimes',color='Purple') #assigns y-label to the plot
    plt.title('Neighborhood Vs Number of Crimes',color='Purple')  #assigns title to the plot
    st.pyplot(fig)
    st.write('This Bar graph illustrates the neighbourhood and intensity of crime in Atlanta, US. The intensity of crime is the highest in Mellwood followed by Ben Hill Pines and Huntington respectively. These neighborhoods are deemed unsafe relative to the other neighborhoods in Atlanta.')
    st.subheader('Play with the Graph:')
    st.plotly_chart(fig) #re-displays the plot with interactive plot interface
    neigh_list = df['neighborhood'].unique() #creates list of all unique neighborhood
    ch = st.checkbox('Display the Corresponding Neighborhood with Numbers in X-axis')  #allows user to choose if they want neighborhood names to be displayed or not
    if ch:  #if checked
        for i, x in enumerate(neigh_list):             #displays enumerated name of neighborhood
            st.write('{0}. {1}'.format(i, repr(x)))

def plot2():
    '''Function to display average crime ratios with their types in a piechart. Provie a user interactive plot interface for zooming in/out ,
     supports manual graph movements with the cursor'''
    fig = plt.figure()
    c_neigh2 = df['number'].groupby(df['crime']).mean()  #calculates the mean number of each crime
    c_neigh=['AGG ASSAULT',             
    'AUTO THEFT',             
    'BURGLARY-NONRES',         
    'BURGLARY-RESIDENCE',      
    'HOMICIDE',                
    'LARCENY-FROM VEHICLE',        #creates a list of the legends
    'LARCENY-NON VEHICLE',     
    'RAPE',                    
    'ROBBERY-COMMERCIAL',      
    'ROBBERY-PEDESTRIAN',      
    'ROBBERY-RESIDENCE'       ]  
    c_neigh2.plot(kind='pie', figsize=(6, 6), radius = 1, labels = None)   #plots the piechart
    plt.legend( labels = c_neigh, bbox_to_anchor=(1.3, 1.15), prop={'size':8}) #displays the corresponding legend
    st.pyplot(fig)
    st.write('The pie chart illustrates the crime ratio in Atlanta, US from 2009- 2017 AD. According to the graph Homicide is the greatest percentage of occurring crimes. Homicide accounts for 99% of the pie chart with all the other crimes together amounting to just 1%. Homicide is the killing of one human being by another.')
    st.subheader('Play with the Graph:')
    fig_html = mpld3.fig_to_html(fig)         # re- displays the plot with interactive plot interface
    components.html(fig_html, height=600)

def plot3():
    '''Funtion to display Average Crime Frequency VS Time as a line graph. Provie a user interactive plot interface for zooming in/out , 
    supports manual graph movements with the cursor'''
    st.header('Crime Frequency Vs Time (2009 - 2017 AD, Atlanta, USA)')
    #xaxis= [2009, 2010, 2011, 2012 ,2013 ,2014 ,2015, 2016, 2017]
    fig = plt.figure()
    c_neigh3 = df['number'].groupby(df.date.dt.to_period('y')).mean()  #calculates the mean number of crimes in each year
    c_neigh3.plot(x='year', y='number', figsize = (10,7))      #plots the line graph
    plt.title('Crime Frequency vs Time',color='orange')
    plt.ylabel('No. of Crimes',color='orange')   #assigns y-label to the plot
    plt.xlabel('Years',color='orange')           #assigns x-label to the plot
    plt.grid()  #displays the plot grid
    st.pyplot(fig)
    st.write('This graph represents the Crime frequency in Atlanta, US from 2009 to 2017 AD. There is an increase in crime rate from 2009 to 2017 with the maximum increase in 2015 as the line is the steepest there. The crime rate experiences a steady increase from 2010 to 2013.')
    st.subheader('Play with the Graph:')
    st.plotly_chart(fig)  # re- displays the plot with interactive plot interface
    

def interactive_plot():
    '''Function to display line/scatter plots from Crime VS Time in a User-chosen Neighbothood,  provie a user interactive plot interface for zooming in/out , 
    supports manual graph movements with the cursor'''
    df = pd.read_csv('atlcrime.csv',usecols=[1,2,3,6]) #reads the data set
    neigh_list = df['neighborhood'].unique()    #creates a list of all unique neigborhood from the dataset
    type = ['Scatter','Line']
    opt=st.selectbox('Select the Neighborhood',options = neigh_list)  #generates a selecbox option for the user to choose the Neighborhood
    opt2 = st.selectbox('Select the type of graph you want for display',options = type) #generates a selectbox option for the user to choose the type of graph they want ot be displayed
    neigh = pd.DataFrame(df.loc[df['neighborhood'] == opt])   #generates new data from each neighborhood as chosen by the user
    neigh['date'] = pd.to_datetime(df.date, format = "%m/%d/%Y")  # create a new data frame with ordered dates in particular format
    neigh['number'].groupby(neigh.date.dt.to_period('y')).mean()  # calculats the mean of number of crimes per year 
    if opt2 == 'Scatter':  #if user chooses Scatter
        plot = px.scatter(df,neigh['date'],neigh['number'],log_y=[8e7,2e11],labels={'x':'Years', 'y':'Crime Intensity'}) #plot the scatter plot with x and y labels
    if opt2 == 'Line':
        plot = px.line(df,neigh['date'],neigh['number'],log_y=[8e7,2e11],labels={'x':'Years', 'y':'Crime Intensity'})   #plot the line graph with x and y labels
    st.plotly_chart(plot)
    st.subheader('Please use the zoom option available to get Monthly, Daily data trends.')
    st.warning('!!! IMPORTANT !!!')                                                   #display a warning message
    st.warning('The  Crime Report dataset accounts for minimum of 200,000 single entries. The evaluated data might have some outliers and errors in a few neighborhoods during the data collection process itself. We donot boast 100 % accuracy in the plots. Please ignore the minor erros and outliers here. Thank you.')
    
with st.sidebar:    #Creates a sidebar for User-Interaction 
    selected = option_menu("Menu", ["Home","About Us", 'Data', 'Plot I','Plot II','Plot III','Interactive Plot'], #set options and add icons to the menu bar
        icons=['house','person', 'gear'], menu_icon="cast", default_index=1,orientation= 'vertical')
    selected

with st.sidebar:
    with st.spinner("Loading..."): #add a 'Loading' animation to the Sidebar whenever the page is loading
        time.sleep(3) #goes maximum until 3 seconds
    st.success(" ")

if selected =='Home':       #if the user chooses Home
    st.title('Welcome to Interactive Web-Based Data Visuals.')  #display page title
    response= requests.get('https://www.sydney.edu.au/content/dam/corporate/images/faculty-of-engineering-and-information-technologies/research/data-science-and-computer-engineering/big-data-visualisation.jpg')
    image11 = Image.open(BytesIO(response.content))  # display images using Get Request by striping them from the internet
    st.image(image11,caption = None , width = 700)
    response11 = requests.get('https://www.analyticsinsight.net/wp-content/uploads/2020/04/data-visualization.jpg')
    image22 = Image.open(BytesIO(response11.content)) # display images using Get Request by striping them from the internet
    st.image(image22,caption = None, width = 700)

elif selected=='About Us': #if the user chooses About Us
    st.title('About Us')  #display the page title
    st.header('Creators:') #display the page header
    about_us()  #call the function

elif selected == 'Data': #if user chooses Data
    st.header('Atlanta, USA Crime Report 2009-2017 AD')  #display the page header
    st.write(df) #display the dataset
    st.write('Data Source: data.world. (n.d.). Data.world. Retrieved October 11, 2022')   #display data source
    st.write('Link : https://data.world/bryantahb/crime-in-atlanta-2009-2017/workspace/file?filename=atlcrime.csv') #cite the link

elif selected =='Plot I': #if user chooses Plot I
    st.header('Neighborhood and Intensity of Crime Bar Graph') #display the header
    plot1()  #call the function 
   
elif selected =='Plot II': #if user chooses Plot II
    st.header('Crime Ratio Pie Chart (2009 - 2017 AD, Atlanta, USA)') #display the header
    plot2()   #call the function
    
elif selected == 'Plot III': #if user chooses Plot III
    plot3()     #call the function 
    
    
elif selected == 'Interactive Plot': #if user chooses Interactive Plot 
    st.header('Crime VS Time of a Particular Neighborhood in Atlanta, USA') #display the header
    interactive_plot()  #call the funtion 
    st.write("")
    st.write('')        #creates line spacing
    st.write('')
    st.write('Was this Page Helpful? ')  #display the message
    a = st.button('Like 👍'  )  #creates Like button
    b = st.button('Unlike 👎')  #creates Unlike Button
    if a :   #if user chooses Like
        st.write('Thank you for your Feedback.🙂') #display the message
    if b:    #if user chooses Unlike
        with st.form(key="forml"): #generate a form
            st.write('How may we improve?') #display the message
            firstname = st.text_input('Firstname') #ask for user's FirstName
            lastname = st.text_input('Lastname')   #ask for user's Lastname
            suggestion = st.text_input('Suggestion') #ask for suggestion from the user
            submitted = st.form_submit_button("Submit")  #create a submit button
            st.write('We will look over your issue. Thank you. 🙂') #display the message
