from django.urls import path
from . import views

# https://docs.djangoproject.com/en/4.2/topics/http/urls/
app_name = 'cats'
urlpatterns = [
    path('', views.CatList.as_view(), name='all'),
    path('create/', views.CatCreate.as_view(), name='cat_create'),
    path('<int:pk>/update/', views.CatUpdate.as_view(), name='cat_update'),
    path('<int:pk>/delete/', views.CatDelete.as_view(), name='cat_delete'),
    path('breed/', views.BreedList.as_view(), name='breed_all'),
    path('breed/create/', views.BreedCreate.as_view(), name='breed_create'),
    path('breed/<int:pk>/update/', views.BreddUpdate.as_view(), name='breed_update'),
    path('breed/<int:pk>/delete/', views.BreddDelete.as_view(), name='breed_delete'),
]

# Note that make_ and cats_ give us uniqueness within this application
