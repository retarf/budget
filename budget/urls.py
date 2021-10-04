from django.urls import path
from budget.views import (
    PeriodListView,
    PeriodCreateView,
    PeriodDetailView,
    PeriodDeleteView,
    EntryListView,
    EntryCreateView,
    EntryDetailView,
    EntryDeleteView,
)

urlpatterns = []


# Period
urlpatterns.extend([
    path('period/', PeriodListView.as_view(), name='period-list'),
    path('period/create/', PeriodCreateView.as_view(), name='period-create'),
    path('period/<int:pk>/', PeriodDetailView.as_view(), name='period-detail'),
    path('period/<int:pk>/delete/', PeriodDeleteView.as_view(), name='period-delete'),
])

# Entry
urlpatterns.extend([
    path('entry/', EntryListView.as_view(), name='entry-list'),
    path('entry/<int:pk>/', EntryDetailView.as_view(), name='entry-detail'),
    path('entry/create/', EntryCreateView.as_view(), name='entry-create'),
    path('entry/<int:pk>/delete/', EntryDeleteView.as_view(), name='entry-delete'),
])
