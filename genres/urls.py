from django.urls import path
from . import views


urlpatterns = [
    path('genres/', views.GenreCreateListView.as_view(), name='genre-created-list'),
    path('genres/<int:pk>/', views.GenreRetrieveUpdateDeleteView.as_view(), name='genre-detail-view'),
]
