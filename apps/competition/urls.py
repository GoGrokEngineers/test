from django.urls import path
from .views import CompetitionCreateView, JoinAPIView

urlpatterns = [
    path('create/', CompetitionCreateView.as_view(), name='create-competition')
    # path('join/', JoinAPIView.as_view(), name='join-competition')
    
]
