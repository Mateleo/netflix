#!/usr/bin/env python
# coding: utf-8
import pandas as pd
from GoogleNews import GoogleNews
googlenews = GoogleNews(lang='en',period='7d')

googlenews.search('Netflix')

result = googlenews.result(sort=True)

df=pd.DataFrame(result)
df = df.drop(columns=["img"])
print(df)

df.head(10)
# Export english dataframe into a CSV
df.to_csv('news_Netflix.csv', sep=',', index=False)

for res in result:
  print("Title : ",res["title"])
  print("News : ",res["desc"])
  print("Detailed news : ",res["link"])
