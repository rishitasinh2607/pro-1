import requests
from bs4 import BeautifulSoup
import pprint
res = requests.get('https://news.ycombinator.com/')
res2 = requests.get('https://news.ycombinator.com/news?p=2') #FOR SECOND PAGE
soup = BeautifulSoup(res.text,'html.parser')
soup = BeautifulSoup(res2.text,'html.parser')
links = soup.select('.storylink') #css selecter play role in background in sorting out
subtext = soup.select('.subtext')
links2= soup.select('.storylink') #css selecter play role in background in sorting out
subtext2 = soup.select('.subtext')

mega_links=links+links2
mega_subtext=subtext+subtext2

def sort_stories_by_voters(hnlist):
    return sorted(hnlist,key=lambda k:k['votes'],reverse=True) #for top stories to be on top  #sort in order

def create_custom_hn(links,subtext):
  hn=[]
  for idx,item in enumerate(links):
      title = item.getText()
      href = item.get('href',None)
      vote = subtext[idx].select('.score')
      if len(vote):

         point = int(vote[0].getText().replace('points',' '))
         if point>99: #allow to filter
           hn.append({'title':title,'link':href,'votes':point})
  return sort_stories_by_voters(hn)

  return hn
pprint.pprint(create_custom_hn(mega_links,mega_subtext))