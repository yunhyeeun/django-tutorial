from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/overview/', views.LocalView.as_view(), name='local'),
    path('<int:pk>/city/', views.CityView.as_view(), name='city'),

]