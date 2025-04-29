from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Retailer

class RetailerListView(ListView):
    model = Retailer
    template_name = 'retailers/retailer_list.html'
    context_object_name = 'retailers'

    def get_queryset(self):
        return Retailer.objects.filter(is_visible=True)

class RetailerDetailView(DetailView):
    model = Retailer
    template_name = 'retailers/retailer_detail.html'
    context_object_name = 'retailer'

    def get_queryset(self):
        return Retailer.objects.filter(is_visible=True)
from django.views.generic import ListView, DetailView
from .models import Retailer

class RetailerListView(ListView):
    model = Retailer
    template_name = 'retailers/retailer_list.html'
    context_object_name = 'retailers'

    def get_queryset(self):
        return Retailer.objects.filter(is_visible=True)

class RetailerDetailView(DetailView):
    model = Retailer
    template_name = 'retailers/retailer_detail.html'
    context_object_name = 'retailer'

    def get_queryset(self):
        return Retailer.objects.filter(is_visible=True)
