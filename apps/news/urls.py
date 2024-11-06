from django.urls import path

from .views import *

urlpatterns = [
    path('news/', NewsCreateAPIView.as_view(), name='create_news'),
    path('news/all/', NewsListAPIView.as_view(), name='get_all_news'),
    path('news/<int:pk>/', NewsRetrieveAPIView.as_view(), name='get_news'),
    path('news/update/<int:pk>/', NewsUpdateAPIView.as_view(), name='update_news'),
]
