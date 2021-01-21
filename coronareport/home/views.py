from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from django.db import models

from .models import Local, City

class IndexView(generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'overview_data'
    
    def get_queryset(self):
        context = {
            'weekly_report_list': Local.objects.order_by('-statedt')[:7]
        }
        context['daily_city_list'] = City.objects.filter(stdday=getattr(context['weekly_report_list'][0],'statedt')).order_by('seq')
        today = context['weekly_report_list'][0]
        yesterday = context['weekly_report_list'][1]
        netchange = {}
        for field in today._meta.fields:
            if isinstance(field, models.IntegerField):
                netchange[field.name] = getattr(today, field.name) - getattr(yesterday, field.name)
        context['net_change'] = netchange
        return context

class LocalView(generic.DetailView):
    model = Local
    template_name = 'home/local.html'
    context_object_name = 'report'

class CityView(generic.DetailView):
    model = City
    template_name = 'home/city.html'
    context_object_name = 'report'
