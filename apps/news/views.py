from django.shortcuts import render
from rest_framework.generics import *

from .models import News
from .serializers import *
# Create your views here.


class NewsCreateAPIView(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsRetrieveAPIView(RetrieveDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    
class NewsUpdateAPIView(UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsUpdateSerializer