from typing import Type

from django.views.generic import ListView, DetailView, CreateView, DeleteView

from budget.models import Period, Entry
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


class EntryListView(ListView):
    model: Type[Period] = Entry


class EntryDetailView(DetailView):
    model: Type[Period] = Entry


class EntryCreateView(CreateView):
    model: Type[Period] = Entry
    fields = '__all__'
    success_url = reverse_lazy('entry-list')


class EntryUpdateView(DetailView):
    model: Type[Period] = Entry


class EntryDeleteView(DeleteView):
    model: Type[Period] = Entry
    success_url = reverse_lazy('entry-list')
#