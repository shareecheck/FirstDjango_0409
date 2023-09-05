from django.urls import path
from MainApp import views


urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('items/', views.items_list),
    path('item/<int:item_id>/', views.item_info)
]
