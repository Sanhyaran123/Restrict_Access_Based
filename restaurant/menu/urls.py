from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuListCreateView.as_view(), name='menu-list-create'),
    path('<int:pk>/', views.MenuRetrieveUpdateDestroyView.as_view(), name='menu-detail'),
]