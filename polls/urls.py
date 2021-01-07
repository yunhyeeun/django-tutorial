from django.conf.urls import url
from django.urls import path
from . import views

'''
path (ROUTE, VIEW, KWARGS, NAME)

1. ROUTE : URL 패턴을 가진 문자열
    - GET, POST 등의 parameter 무시

2. VIEW

3. KWARGS

4. NAME

'''

urlpatterns = [
    path('', views.index, name='index'),
]