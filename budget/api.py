from rest_framework import viewsets
from rest_framework.response import Response

from budget.serializers import PeriodSerializer, EntrySerializer
from budget.models import Period, Entry


class PeriodViewSet(viewsets.ModelViewSet):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
