from django.urls import path

from .views import *

urlpatterns = [
    path('', NewsAPIView.as_view(), name="settings list api"),
    path('<int:pk>/', SettingsRetrieveAPI.as_view(), name="settings retrive api"),
]