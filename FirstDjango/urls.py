from django.urls import path
from MainApp import views


urlpatterns = [
    path('', views.home),
    path('about/', views.users),
    path('item/<int:id>/', views.products)
]
