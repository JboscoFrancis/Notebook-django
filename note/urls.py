from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<str:pk>', views.notedel, name='delete'),
    path('detail/<str:pk>', views.detail, name='detail'),
    path('complete/', views.complete, name='complete'),
]
