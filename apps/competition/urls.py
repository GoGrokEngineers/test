from django.urls import path
from .views import CompetitionCreateView, CompetitionListView

urlpatterns = [
    path('create/', CompetitionCreateView.as_view(), name='create-competition'),
    path('get/', CompetitionListView.as_view(), name='list-competitions'),
]
