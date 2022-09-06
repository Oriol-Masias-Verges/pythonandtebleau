#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 17:35:57 2022

@author: uri
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# reading excel or xlsx files
data = pd.read_excel('articles.xlsx')

# summary of the information
data.describe()
data.info()

# counting the number of articles per source
data.groupby(['source_id'])['article_id'].count()


# number of reactions by publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()

# dropping a column
data = data.drop('engagement_comment_plugin_count', axis=1)


# Functions in Python

def thisFunction():
    print('This is my First Function')


thisFunction()

# This is a function with variables


def aboutMe(name, surname, location):
    print('This is ' + name + '. My surname is ' + surname
          + ' and I am from ' + location + '.')
    return name, surname, location


a = aboutMe('Uri', 'Masias', 'Barcelona')

# Using for loops in functions


def favfood(food):
    for x in food:
        print('top food is ' + x)


fastfood = ['salad', 'water', 'fruit']
more_fast_fod = ['apple', 'pear']

favfood(fastfood)
favfood(more_fast_fod)

# creating a keyword flag

length = len(data)
keyword = 'crash'

# lets create a for loop to isolate each title row
# creating a function


def keywordflag(keyword):
    length = len(data)
    keyword_flag = []
    for x in range(0, length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag


keywordflag = keywordflag('murder')


# creating a new column in data dataframe
data['keyword_flag'] = pd.Series(keywordflag)


# SentimentIntensityAnalyzer
sent_int = SentimentIntensityAnalyzer()
title_sent_anal = sent_int.polarity_scores(data['title'][100])

# adding a for loop to extract sentiment per title

title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []
for x in range(0, length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)

title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)

data['title_neg_sentiment'] = title_neg_sentiment
data['title_pos_sentiment'] = title_pos_sentiment
data['title_neu_sentiment'] = title_neu_sentiment

# writing the data
data.to_excel('blogme_clean.xlsx', sheet_name='blogmedata', index=False)
