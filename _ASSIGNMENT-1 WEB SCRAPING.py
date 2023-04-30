#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Q1 - 1)	rite a python program to displaWy all the header tags from wikipedia.org and make data frame.


# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/Main_Page"
response = requests.get(url)


soup = BeautifulSoup(response.content, "html.parser")
e
headers = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])


header_texts = []

# Loop through each header tag and append its text to the list
for header in headers:
    header_texts.append(header.text)

# Create a Pandas DataFrame from the list of header tag text
df = pd.DataFrame(header_texts, columns=["Header"])

# Print the DataFrame
print(df)


# In[ ]:


Q2- 2)	Write a python program to display IMDB’s Top rated 50 movies’ data (i.e. name, rating, year of release) and make data frame.


# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.imdb.com/chart/top/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

titles = []
ratings = []
years = []

movie_data = soup.select("td.titleColumn")
rating_data = soup.select("td.posterColumn span[name='ir']")
year_data = soup.select("td.titleColumn span.secondaryInfo")

for i in range(0, 51):
    title = movie_data[i].a.text
    titles.append(title)

    rating = float(rating_data[i]['data-value'])
    ratings.append(rating)

    year = year_data[i].text
    years.append(year)

movies = pd.DataFrame({
    "title": titles,
    "rating": ratings,
    "year": years
})

print(movies)


# In[ ]:


Q3 - 3)	Write a python program to display IMDB’s Top rated 50 Indian movies’ data (i.e. name, rating, year of release) and make data frame.


# In[2]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send a request to the IMDb page and extract the HTML content
url = 'https://www.imdb.com/india/top-rated-indian-movies/'
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the movie list table and extract its rows
movie_table = soup.find('tbody', class_='lister-list')
movie_rows = movie_table.find_all('tr')

# Create empty lists to store movie data
movie_names = []
movie_ratings = []
movie_years = []

# Extract movie data from each row and append it to the respective list
for row in movie_rows:
    movie_name = row.find('td', class_='titleColumn').a.text
    movie_names.append(movie_name)

    movie_rating = float(row.find('td', class_='ratingColumn imdbRating').strong.text)
    movie_ratings.append(movie_rating)

    movie_year = int(row.find('td', class_='titleColumn').span.text.strip('()'))
    movie_years.append(movie_year)

# Create a pandas dataframe with the extracted movie data
df = pd.DataFrame({
    'Name': movie_names,
    'Rating': movie_ratings,
    'Year': movie_years
})

# Display the dataframe
print(df)


# In[ ]:


Q4 - 4)	Write s python program to display list of respected former presidents of India(i.e. Name , Term ofoffice) from https://presidentofindia.nic.in/former-presidents.htm and make data frame.


# In[3]:


from bs4 import BeautifulSoup
import requests
page=requests.get('https://presidentofindia.nic.in/former-presidents.htm')
page
soup=BeautifulSoup(page.content)
soup
first_title=soup.find('h3')
first_title
first_title=soup.find('h3')
first_title
first_title=[]
for i in soup.find_all('h3'):
    first_title.append(i.text)
first_title
Term=soup.find('p')
Term
Term.text
Term=[]
for i in soup.find_all('p'):
    Term.append(i.text)
Term

Detail=soup.find('div', class_="presidentListing")
Detail
Detail.text
Detail=[]
for i in soup.find_all('div', class_="presidentListing"):
    Detail.append(i.text)
Detail
import pandas as pd
df=pd.DataFrame({"PresidentiaL List":Detail})
df


# In[ ]:


Q5 - 5)	Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame-
A - a)	Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.


# In[4]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send a GET request to the URL of the ODI team rankings page
url = 'https://www.icc-cricket.com/rankings/mens/team-rankings/odi'
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the table containing the team rankings data
table = soup.find('table', class_='table')

# Extract the data from the table and store it in lists
teams = []
matches = []
points = []
ratings = []

for row in table.tbody.find_all('tr'):
    team = row.find('span', class_='u-hide-phablet').text.strip()
    match = row.find_all('td')[2].text.strip()
    point = row.find_all('td')[3].text.strip()
    rating = row.find_all('td')[4].text.strip()
    teams.append(team)
    matches.append(match)
    points.append(point)
    ratings.append(rating)

# Create a pandas data frame to display the data
data = {'Team': teams, 'Matches': matches, 'Points': points, 'Rating': ratings}
df = pd.DataFrame(data)
df.index += 1  # Start the index from 1
df = df.head(10)  # Display only the top 10 teams
print(df)


# In[ ]:


B = b)	Top 10 ODI Batsmen along with the records of their team andrating.


# In[5]:


req=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting')
soup=BeautifulSoup(req.content)
player=soup.find_all('tr',class_=('rankings-block__banner','table-body'))
top10=player[0:10]
data={'Player_Name':[],'Team_Name': [], 'Rating':[]}
for i in top10:
    bat=i.find_all('td',recursive=True)
    data['Player_Name'].append(bat[1].text.replace('\n',''))
    data['Team_Name'].append(bat[2].text.replace('\n',''))
    data['Rating'].append(bat[3].text.replace('\n',''))
ODIBATSMAN=pd.DataFrame(data,index=range(1,11))
ODIBATSMAN


# In[ ]:


c)	Top 10 ODI bowlers along with the records of their team andrating.


# In[6]:


req=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling')
soup=BeautifulSoup(req.content)
bowler=soup.find_all('tr',class_=('rankings-block__banner','table-body'))
Top10=bowler[0:10]
bdata={'Player_Name':[],'Team_Name': [], 'Rating':[]}
for i in Top10:
    bat=i.find_all('td',recursive=True)
    bdata['Player_Name'].append(bat[1].text.replace('\n',''))
    bdata['Team_Name'].append(bat[2].text.replace('\n',''))
    bdata['Rating'].append(bat[3].text.replace('\n',''))
ODIBOWL=pd.DataFrame(bdata,index=range(1,11))
ODIBOWL


# In[ ]:


6)	Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame-
a)	Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.


# In[7]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
req=requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')
soup=BeautifulSoup(req.content)
team=soup.find_all('tr',class_=('rankings-block__banner','table-body'))
top10=team[0:10]
data = {'Team_Name':[],'Matches': [],'Points': [],'Rating':[]}

for i in top10:
    pnt=i.find_all('td',recursive=True)
    data['Team_Name'].append(i.find('span',class_='u-hide-phablet').text)
    data['Matches'].append(pnt[2].text)
    data['Points'].append(pnt[3].text)
    data['Rating'].append(pnt[4].text.strip().replace('\n',''))
WomenTeam=pd.DataFrame(data,index=range(1,11))
WomenTeam


# In[ ]:


b)	Top 10 women’s ODI Batting players along with the records of their team and rating.


# In[8]:


req=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting')
soup=BeautifulSoup(req.content)
player=soup.find_all('tr',class_=('rankings-block__banner','table-body'))

top10=player[0:10]
data={'Player_Name':[],'Team_Name': [], 'Rating':[]}

for i in top10:
    bat=i.find_all('td',recursive=True)
    data['Player_Name'].append(bat[1].text.replace('\n',''))
    data['Team_Name'].append(bat[2].text.replace('\n',''))
    data['Rating'].append(bat[3].text.replace('\n',''))
BATW=pd.DataFrame(data,index=range(1,11))  
BATW


# In[ ]:


c)	Top 10 women’s ODI all-rounder along with the records of their team and rating.


# In[9]:


req=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder')
soup=BeautifulSoup(req.content)
player=soup.find_all('tr',class_=('rankings-block__banner','table-body'))

top10=player[0:10]
data={'Player_Name':[],'Team_Name': [], 'Rating':[]}

for i in top10:
    bat=i.find_all('td',recursive=True)
    data['Player_Name'].append(bat[1].text.replace('\n',''))
    data['Team_Name'].append(bat[2].text.replace('\n',''))
    data['Rating'].append(bat[3].text.replace('\n',''))
W_All=pd.DataFrame(data,index=range(1,11))
W_All


# In[ ]:


7)	Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world and make data frame-
i)	Headline
ii)	Time
iii)	News Link


# In[10]:


import requests
from bs4 import BeautifulSoup
page=requests.get('https://www.cnbc.com/world/?region=world')
page
news=BeautifulSoup(page.content)
news
# Headline
Headline=[]
for i in news.find_all('div',class_='RiverHeadline-headline RiverHeadline-hasThumbnail'):
   Headline.append(i.text)
Headline
# Time
Time=news.find('time')
Time
Time.text
Time=[]
for i in news.find_all('time'):
   Time.append(i.text)
Time
# Newslink
url = "https://www.cnbc.com/world/?region=world"
webpage = requests.get(url) 
trav = BeautifulSoup(webpage.content, "html.parser")
for link in trav.find_all('a'):
    print(type(link), " ", link)
trav.text


# In[ ]:


8)	Write a python program to scrape the details of most downloaded articles from AI in last 90 days.https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles Scrape below mentioned details and make data frame-
i)	Paper Title
ii)	Authors
iii)	Published Date
iv)	Paper URL


# In[11]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

titles = []
authors = []
dates = []
urls = []

articles = soup.find_all('li', class_='pod-listing is-article')
for article in articles:
    title = article.find('a', class_='pod-listing__title').text.strip()
    titles.append(title)
    
    author = article.find('span', class_='pod-listing__author-name').text.strip()
    authors.append(author)
    
    date = article.find('span', class_='pod-listing__meta-date').text.strip()
    dates.append(date)
    
    url = article.find('a', class_='pod-listing__title')['href']
    urls.append(url)

data = {'Paper Title': titles, 'Authors': authors, 'Published Date': dates, 'Paper URL': urls}
df = pd.DataFrame(data)
print(df)


# In[ ]:


9)	Write a python program to scrape mentioned details from dineout.co.in and make data frame-
i)	Restaurant name
ii)	Cuisine
iii)	Location
iv)	Ratings
v)	Image URL



# In[12]:


import requests
from bs4 import BeautifulSoup
page=requests.get('https://www.dineout.co.in/delhi-restaurants/welcome-back')
page
soup=BeautifulSoup(page.content)
soup
# Restaurant Name
RN=soup.find('div',class_="restnt-info cursor")
RN
RN.text
RN=[]
for i in soup.find_all('div',class_="restnt-info cursor"):
    RN.append(i.text)
RN
# Cusines
price=[]
for i in soup.find_all('span',class_="double-line-ellipsis"):
    price.append(i.text)
price
# Location
location=[]
for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    location.append(i.text)
location
# Images
images=[]
for i in soup.find_all('img',class_="no-img"):
    images.append(i['data-src'])
images





# In[ ]:




