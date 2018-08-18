import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

# Create your views here.
# Function based views

class HomeView(TemplateView):
    template_name='home.html'

    def get_context_data(self, *args, **kwargs):
        context=super(HomeView, self).get_context_data(*args, **kwargs)
        num=None
        some_list=[
            random.randint(0,1000000),
            random.randint(0,1000000),
            random.randint(0,1000000)
       ]
        condition_bool_item=False
        if condition_bool_item:
            num= random.randint(0,1000000)
        context= {
            "num": num,
            "some_list": some_list
        }
        return context