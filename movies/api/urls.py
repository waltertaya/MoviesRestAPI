from os import name
from django.urls import path
from . import views


urlpatterns = [
    path('api/v1/', views.MoviesListCreate.as_view(), name='movies-list-create-view'),
    path('api/v1/<int:pk>/', views.MoviesRetrieveUpdateDestroy.as_view(), name='update')
]
