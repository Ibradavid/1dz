from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import News
from .serializers import *
# Create your views here.


class NewsAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class SettingsRetrieveAPI(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
