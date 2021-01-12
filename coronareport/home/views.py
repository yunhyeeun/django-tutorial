from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import generic

from .models import Local, City

class IndexView(generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'latest_report_list'

    def get_queryset(self):
        return Local.objects.order_by('-statedt')[:1]

class LocalView(generic.DetailView):
    model = Local
    template_name = 'home/local.html'
    context_object_name = 'report'

class CityView(generic.DetailView):
    model = City
    template_name = 'home/city.html'
    context_object_name = 'report'
