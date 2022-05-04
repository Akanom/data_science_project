#!/usr/bin/env python
# coding: utf-8

# # <h1>Extracting and Visualization of Stock Data</h1>
# <h2>Description</h2>

# <h2>Table of contents</h2>
# <div class="alert alert-block alert-info" style="margin-top: 20px">
# <li>
#     <ul>Define a function to make a graph</ul>
#     <ul>Extract stock Tesla data</ul>
#     <ul>Use webscrapping to extract Tesla revenue</ul>
#     <ul>Extract stock Amazon data</ul>
#     <ul>Use webscrapping to extract Amazon revenue</ul>
#     <ul>Extract stock Twitter data</ul>
#     <ul>Use webscrapping to extract Twitter revenue</ul>
#     <ul> Plot Tesla stock </ul>
#     <ul>Plot Amazon stock</ul>
#     <ul>Plot Twitter stock</ul>
# </li>

# In[1]:


import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# <h2>Define a function to make the graphs</h2>
# <p>This section will define the functions that will be used to plot the graphs. It takes a dataframe that contains the stock, a dataframe that contains the revenue and the name of the stock</p>

# In[2]:


def graph(stock, revenue, name_of_stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Share Price", "Share Revenue"), vertical_spacing = .5)
    stock_data = name_share_price[name_share_price.Date <= '2022-04-30']
    revenue_data = name_revenue[revenue_data.Date <= '2022-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()


# <h2>Extracting Tesla stock</h2>
# <p>The Ticker method is used to extract Tesla stock data to create an object. The Tesla stock Ticker symbol is TSLA</p>

# In[3]:


tesla=yf.Ticker("TSLA")


# In[4]:


tesla_info=tesla.info


# <p>The Ticker object and function history extract stock infomation and save into a dataframe tesla data. The period pariod parameter is set to max so we get the maximum amount of time</p>

# In[5]:


Tesla_share_price=tesla.history(period="max")


# <p>The reset_index(inplace=True) function is used to set the index function. The head method is used to display the first five rows of the data.</p>

# In[6]:


Tesla_share_price.reset_index(inplace=True)


# In[7]:


Tesla_share_price.head()


# <h2>Extracting Tesla revenue by webscrapping</h2>
# <p>The request library is used to download the webpage from <a href="https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue">visit macrotrends website</a></p>

# In[8]:


Tesla_html="https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"


# In[9]:


Tesla_request=requests.get(Tesla_html).text


# <p>BeautifulSoup is used to to parse the data</p>

# In[10]:


Tesla_soup=BeautifulSoup(Tesla_request,"html.parser")


# <p>BeautifulSoup is used to extract Tesla Quarterly revenue and stored in Tesla_revenue</p>

# In[11]:


tesla_revenue=pd.DataFrame(columns=["Date", "Revenue"])
for rows in Tesla_soup.find_all("tbody")[1].find_all("tr"):
    col=rows.find_all("td")
    date=col[0].text
    quarterly_revenue=col[1].text
    
    tesla_revenue=tesla_revenue.append({"Date":date,"Revenue":quarterly_revenue},ignore_index=True)
tesla_revenue.head()
    


# <p>The comma and dollar signs are removed with the following commands</p>

# In[12]:


tesla_revenue["Revenue"]=tesla_revenue["Revenue"].str.replace(",|\$","")


# <p>The following code remove the empty string in the revenue column</p>

# In[13]:


tesla_revenue.dropna(inplace=True)
tesla_revenue=tesla_revenue[tesla_revenue["Revenue"]!=""]


# In[14]:


tesla_revenue.head()


# <h2>Extracting Amazon stock</h2>
# <p>The Ticker method is used to extract amazon stock. The Amazon stock ticker is AMZN.</p>

# In[15]:


Amazon=yf.Ticker("AMZN")


# In[16]:


amazon_info=Amazon.info


# <p>The Ticker object and function history extract stock infomation and save into a dataframe amazon stock data. The period pariod parameter is set to max so we get the maximum amount of time</p>

# In[17]:


Amazon_share_price=Amazon.history(period="max")


# <p>The reset_index(inplace=True) function is used to set the index function. The head method is used to display the first five rows of the data.</p>

# In[18]:


Amazon_share_price.reset_index(inplace=True)


# In[19]:


Amazon_share_price.head()


# <h2>Extracting Amazon revenue by webscrapping</h2>
# <p>The request library is used to download the webpage from <a href="https://www.macrotrends.net/stocks/charts/AMZN/amazon/revenue" rel="import">visit macrotrends website</a> </p>

# In[20]:


Amazon_html="https://www.macrotrends.net/stocks/charts/AMZN/amazon/revenue"


# In[21]:


Amazon_request=requests.get(Amazon_html).text


# <p>BeautifulSoup is used to to parse the data</p>

# In[22]:


Amazon_soup=BeautifulSoup(Amazon_request,"html.parser")


# <p>BeautifulSoup is used to extract Amazon Quarterly revenue and stored in Tesla_revenue</p>

# In[23]:


amazon_revenue=pd.DataFrame(columns=["Date", "Revenue"])
for rows in Amazon_soup.find_all("tbody")[1].find_all("tr"):
    col=rows.find_all("td")
    date=col[0].text
    quarterly_revenue=col[1].text
    
    amazon_revenue=amazon_revenue.append({"Date":date,"Revenue":quarterly_revenue},ignore_index=True)
amazon_revenue.head()
    


# <p>The comma and dollar signs are removed with the following commands</p>

# In[24]:


amazon_revenue["Revenue"]=amazon_revenue["Revenue"].str.replace(",|\$","")


# <p>The following code remove the empty string in the revenue column</p>

# In[25]:


amazon_revenue.dropna(inplace=True)
amazon_revenue=amazon_revenue[amazon_revenue["Revenue"]!=""]


# In[26]:


amazon_revenue.head()


# <h2>Extracting Twitter stock</h2>
# <p>The Ticker method is used to extract twitter stock. The Twitter stock ticker is TWTR.</p>

# In[27]:


Twitter=yf.Ticker("TWTR")


# In[28]:


twitter_info=Twitter.info


# <p>The Ticker object and function history extract stock infomation and save into a dataframe amazon stock data. The period pariod parameter is set to max so we get the maximum amount of time</p>

# In[29]:


Twitter_share_price=Twitter.history(period="max")


# <p>The reset_index(inplace=True) function is used to set the index function. The head method is used to display the first five rows of the data.</p>

# In[30]:


Twitter_share_price.reset_index(inplace=True)


# In[31]:


Twitter_share_price.head()


# <h2>Extracting Amazon revenue by webscrapping</h2>
# <p>The request library is used to download the webpage from <a href="https://www.macrotrends.net/stocks/charts/TWTR/twitter/revenue" rel="import">visit macrotrends website</a> </p>

# In[32]:


Twitter_html="https://www.macrotrends.net/stocks/charts/TWTR/twitter/revenue"


# In[33]:


Twitter_request=requests.get(Twitter_html).text


# <p>BeautifulSoup is used to to parse the data</p>

# In[34]:


Twitter_soup=BeautifulSoup(Twitter_request,"html.parser")


# <p>BeautifulSoup is used to extract Amazon Quarterly revenue and stored in Tesla_revenue</p>

# In[35]:


twitter_revenue=pd.DataFrame(columns=["Date", "Revenue"])
for rows in Twitter_soup.find_all("tbody")[1].find_all("tr"):
    col=rows.find_all("td")
    date=col[0].text
    quarterly_revenue=col[1].text
    
    twitter_revenue=twitter_revenue.append({"Date":date,"Revenue":quarterly_revenue},ignore_index=True)
twitter_revenue.head()


# <p>The comma and dollar signs are removed with the following commands</p>

# In[36]:


twitter_revenue["Revenue"]=twitter_revenue["Revenue"].str.replace(",|\$","")


# <p>The following code remove the empty string in the revenue column</p>

# In[37]:


twitter_revenue.dropna(inplace=True)
twitter_revenue=twitter_revenue[twitter_revenue["Revenue"]!=""]


# In[38]:


twitter_revenue.head()


# <h2>Plotting Tesla stock</h2>
# <p>The graph function is used to plot Tesla graph.</p>

# In[39]:


def graph(stock, revenue, name_of_stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Share Price", "Share Revenue"), vertical_spacing = .35)
    stock_data = Tesla_share_price[Tesla_share_price.Date <= '2022-04-30']
    revenue_data = tesla_revenue[tesla_revenue.Date <= '2022-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data.Date, infer_datetime_format=True), y=stock_data.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data.Date, infer_datetime_format=True), y=revenue_data.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=1000,
    title=name_of_stock,
    xaxis_rangeslider_visible=True)
    fig.show()


# In[40]:


graph(Tesla_share_price,tesla_revenue,"Tesla")


# <h2>Plotting Amazon stock</h2>
# <p>The graph function is used to plot Amazon graph.</p>

# In[41]:


def graph(stock, revenue, name_of_stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Share Price", "Share Revenue"), vertical_spacing = .35)
    stock_data = Amazon_share_price[Amazon_share_price.Date <= '2022-04-30']
    revenue_data = amazon_revenue[amazon_revenue.Date <= '2022-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data.Date, infer_datetime_format=True), y=stock_data.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data.Date, infer_datetime_format=True), y=revenue_data.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=1000,
    title=name_of_stock,
    xaxis_rangeslider_visible=True)
    fig.show()


# In[42]:


graph(Amazon_share_price,amazon_revenue,"Amazon")


# <h2>Plotting Twitter stock</h2>
# <p>The graph function is used to plot Twitter graph.</p>

# In[43]:


def graph(stock, revenue, name_of_stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Share Price", "Share Revenue"), vertical_spacing = .35)
    stock_data = Twitter_share_price[Twitter_share_price.Date <= '2022-04-30']
    revenue_data = twitter_revenue[twitter_revenue.Date <= '2022-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data.Date, infer_datetime_format=True), y=stock_data.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data.Date, infer_datetime_format=True), y=revenue_data.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=1000,
    title=name_of_stock,
    xaxis_rangeslider_visible=True)
    fig.show()


# In[44]:


graph(Twitter_share_price,amazon_revenue,"Twitter")


# <h2>About the Author:</h2>
# <p><a href="https://www.linkedin.com/in/oluwajuwon-mayomi-akanbi">Akanbi Oluwajuwon Mayomi</a> has a Master's degree in Economics, his interest are data science, web development, and researchs on international economics </p>
