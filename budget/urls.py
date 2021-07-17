from django.urls import path
from budget.views import PeriodListView, PeriodCreateView, PeriodDetailView

urlpatterns = [
    path('period/', PeriodListView.as_view(), name='period-list'),
    path('period/create/', PeriodCreateView.as_view(), name='period-create'),
    path('period/<int:pk>/', PeriodDetailView.as_view(), name='period-detail'),
]