from django.urls import path
from . import views


urlpatterns = [
    path('actors/', views.ActorCreateListView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>/', views.ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail-view'),
    path('nationalities/', views.NationalityListCreateView.as_view(), name='nationality-create-list'),
    path('nationalities/<int:pk>/', views.NationalityRetrieveUpdateDestroyView.as_view(), name='nationality-detail-list')
]
