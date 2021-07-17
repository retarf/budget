from typing import Type

from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView, CreateView, DeleteView

from budget.models import Period
from django.urls import reverse_lazy
from budget.forms import PeriodForm


class PeriodListView(ListView):
    model: Type[Period] = Period


class PeriodDetailView(DetailView):
    model: Type[Period] = Period


class PeriodCreateView(CreateView):
    model: Type[Period] = Period
    form_class = PeriodForm


class PeriodUpdateView(DetailView):
    model: Type[Period] = Period


class PeriodDeleteView(DeleteView):
    model: Type[Period] = Period
    success_url = reverse_lazy('period-list')
