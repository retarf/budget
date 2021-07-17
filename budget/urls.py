from django.urls import path
from budget.views import PeriodListView, PeriodCreateView, PeriodDetailView, PeriodDeleteView

urlpatterns = [
    path('period/', PeriodListView.as_view(), name='period-list'),
    path('period/create/', PeriodCreateView.as_view(), name='period-create'),
    path('period/<int:pk>/', PeriodDetailView.as_view(), name='period-detail'),
    path('period/<int:pk>/', PeriodDetailView.as_view(), name='period-detail'),
    path('period/<int:pk>/delete/', PeriodDeleteView.as_view(), name='period-delete'),
]