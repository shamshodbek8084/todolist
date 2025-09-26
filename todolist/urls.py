from django.urls import path
from .views import ListView, DetailIdView

urlpatterns = [
    path('', ListView.as_view(), name='list_view'),
    path('<int:id>', DetailIdView.as_view(), name='detail_view'),
]