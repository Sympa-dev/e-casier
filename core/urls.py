from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('request/', request, name='request'),
    path('consultation/', consultation, name='consultation'),
]