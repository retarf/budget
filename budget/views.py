from typing import Type

from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView, CreateView

from budget.models import Period


class PeriodListView(ListView):
    model: Type[Period] = Period


class PeriodDetailView(DetailView):
    model: Type[Period] = Period


class PeriodCreateView(CreateView):
    model: Type[Period] = Period
    fields = ['name']


class PeriodUpdateView(DetailView):
    model: Type[Period] = Period
