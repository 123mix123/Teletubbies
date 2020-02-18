from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime
import csv
from datetime import timedelta
import time
import random

def urlscrap(url,index) :
    #url = input('Enter Youtube Video Url- ') # user input for the link
    Vid={}
    Link = url
    source= requests.get(url).text
    soup=BeautifulSoup(source,'html.parser')
    div_s = soup.findAll('div')[1]
    Subscribers = getSubscribers(div_s)
    Likes = getLikes(div_s)
    Dislikes = getDislikes(div_s)
    Title = div_s.find('meta',itemprop="name").get('content')
    View_count = div_s.find('div',class_="watch-view-count").text.split(' ')[1]
    Duration = div_s.find('meta',itemprop="duration").get('content')
    Description = div_s.find('meta',itemprop="description").get('content')
    Date_upload = div_s.find('meta',itemprop="datePublished").get('content')
    Category = div_s.find('meta',itemprop="genre").get('content')
    text_var = div_s.findAll('script')[1].text
    Tag_index1 = text_var.find('keywords')
    Tag_index2 = text_var.find('channelId')
    Channel_name_index1 = text_var.find('ownerChannelName')
    Channel_name_index2 = text_var.find('uploadDate')
    Channel_name = text_var[ Channel_name_index1+21: Channel_name_index2-5]
    Tag_list = text_var[Tag_index1+11:Tag_index2-3].split('"')[1:-1]
    Tag = []
    for x in Tag_list :
        A = x.strip('\\').strip(',')
        if A != '':
            Tag.append(A)
    time = pd.datetime.utcnow()+timedelta(hours=7)
    Vid['Time'] = time
    Vid['Category']=Category
    Vid['Channel']=Channel_name
    Vid['Subscribers']=Subscribers
    Vid['Link']=Link
    Vid['Title']=Title
    Vid['Date_upload']=Date_upload
    Vid['View']=View_count
    Vid['Duration']=Duration
    Vid['Description']=Description
    Vid['Likes']=Likes
    Vid['Dislikes']=Dislikes
    Vid['Tag']= [Tag]
    Vid_df= pd.DataFrame(Vid,index=[index])
    return Vid_df
#print('asdf')
def appendData(csv_name):
    with open(csv_name+'_data.csv','a',encoding='utf-8') as data :
        with open(csv_name+'.csv','r') as ref_url :
            for i,row in enumerate(ref_url):
                if i > 0 :
                    A = urlscrap(row,i)
                    A.to_csv(data,header=False,sep='|',line_terminator="\n")
                print(i) # to check the number of clips
                t = random.randrange(1,3)
                time.sleep(t)
def getSubscribers(div_s) :
    while True :
        try :
            x = div_s.find('span',class_="yt-subscription-button-subscriber-count-branded-horizontal yt-subscriber-count").text.strip()
            return x
        except ValueError :
            return None
def getLikes(div_s) :
    while True :
        try :
            x = div_s.find('button',class_="yt-uix-button yt-uix-button-size-default yt-uix-button-opacity yt-uix-button-has-icon no-icon-markup like-button-renderer-like-button like-button-renderer-like-button-unclicked yt-uix-clickcard-target yt-uix-tooltip" ).text.strip()
            return x
        except ValueError :
            return None
def getDislikes(div_s) :
    while True :
        try :
            x = div_s.find('button',class_="yt-uix-button yt-uix-button-size-default yt-uix-button-opacity yt-uix-button-has-icon no-icon-markup like-button-renderer-dislike-button like-button-renderer-dislike-button-unclicked yt-uix-clickcard-target yt-uix-tooltip" ).text.strip()
            return x
        except ValueError :
            return None
start = pd.datetime.utcnow()+timedelta(hours=7)
csv_name = input('Please enter your CSV FILE NAME (DONT INCLUDE .CSV): ')
print('before call fuction')
appendData(csv_name)
end = pd.datetime.utcnow()+timedelta(hours=7)
print('Elapsed Timee: ',str(end-start))
