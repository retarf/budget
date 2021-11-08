from rest_framework import serializers

from budget.models import Period, Entry


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = '__all__'


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'
