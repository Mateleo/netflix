from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

import pandas as pd
import json


df = pd.read_csv("dataset/freq.csv", names=["word", "frequency"])
df2 = pd.read_csv("dataset/top2.csv", names=["word", "frequency"])
df3 = pd.read_csv("dataset/top3.csv", names=["word", "frequency"])

df4 = pd.read_csv("dataset/tweet.csv")


def cw1(request):
    return JsonResponse(json.loads(df.to_json(orient="values")), safe=False)

def cw2(request):
    return JsonResponse(json.loads(df2.to_json(orient="values")), safe=False)

def cw3(request):
    return JsonResponse(json.loads(df3.to_json(orient="values")), safe=False)

def tw1(request):
    return JsonResponse(json.loads(df4.to_json(orient="values")), safe=False)

