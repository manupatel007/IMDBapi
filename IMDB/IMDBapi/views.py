from .models import IMDBdata
from django.http import JsonResponse, HttpResponse
from .serializers import IMDBSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
# Create your views here.
'''import pandas as pd

df = pd.read_csv("F:\Internship project\IMDB\IMDBapi\IMDB_final.csv")
for j in range(250):
    val = IMDBdata(Title=df.iloc[j]['Title'], Year=df.iloc[j]['Year'], Rating=df.iloc[j]['IMDb Rating'], ImgUrl=df.iloc[j]['Tumbnail'])
    val.save()'''

'''a = IMDBdata.objects.all()
print(len(a))'''
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def home(request,res=""):
    if(res==""):
        a = IMDBdata.objects.all()
    else:
        if '-' in res:
            val = res.index('-')
            order = res[val+1:]
            ans = res[:val]
            if(order=='desc'):
                a = IMDBdata.objects.all().order_by('-'+ans)
            elif(order=='asc'):
                a = IMDBdata.objects.all().order_by(ans)
            else:
                return JsonResponse({'info':'please check your url'})
        else:
            a = IMDBdata.objects.all().order_by(res)
    serializer = IMDBSerializer(a, many=True)
    return JsonResponse(serializer.data, safe = False)

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def search(request,q=""):
    a = IMDBdata.objects.filter(Title__contains=q)
    serializer = IMDBSerializer(a, many=True)
    return JsonResponse(serializer.data, safe = False)