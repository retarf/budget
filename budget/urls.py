from django.urls import path
from budget.views import (
    PeriodListView,
    PeriodCreateView,
    PeriodDetailView,
    PeriodDeleteView,
    # PlannedListView,
    # PlannedCreateView,
    # PlannedDetailView,
    # PlannedDeleteView,
)

urlpatterns = []


# Period
urlpatterns.extend([
    path('period/', PeriodListView.as_view(), name='period-list'),
    path('period/create/', PeriodCreateView.as_view(), name='period-create'),
    path('period/<int:pk>/', PeriodDetailView.as_view(), name='period-detail'),
    path('period/<int:pk>/delete/', PeriodDeleteView.as_view(), name='period-delete'),
])

# Planned
# urlpatterns.extend([
#     path('period/<int:pk>/planned/', PlannedListView.as_view(), name='planned-list'),
#     path('period/<int:pk>/planned/<int:pk>/', PlannedDetailView.as_view(), name='planned-detail'),
#     path('period/<int:pk>/planned/create/', PlannedCreateView.as_view(), name='planned-create'),
#     path('period/<int:pk>/planned/<int:pk>/delete/', PlannedDeleteView.as_view(), name='period-delete'),
# ])
