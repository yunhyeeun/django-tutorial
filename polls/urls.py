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

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]