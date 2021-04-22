from django.shortcuts import render
from .models import IMDBdata
# Create your views here.
'''import pandas as pd

df = pd.read_csv("F:\Internship project\IMDB\IMDBapi\IMDB_final.csv")
for j in range(250):
    val = IMDBdata(Title=df.iloc[j]['Title'], Year=df.iloc[j]['Year'], Rating=df.iloc[j]['IMDb Rating'], ImgUrl=df.iloc[j]['Tumbnail'])
    val.save()'''

'''a = IMDBdata.objects.all()
print(len(a))'''

def home(request):
    a = IMDBdata.objects.all()
    print(a[0].Title)
