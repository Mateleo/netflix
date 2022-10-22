from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

import pandas as pd
import json


df = pd.read_csv("dataset/fred.csv", names=["word", "frequency"])


def cw1(request):
    return JsonResponse(json.loads(df.to_json(orient="columns")), safe=False)
