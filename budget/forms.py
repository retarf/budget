from django import forms

from budget.models import Period, PlannedEntry, RealEntry


class PeriodForm(forms.ModelForm):
    name = forms.DateField()

    class Meta:
        model = Period
        fields = ['name']


class EntryForm(forms.ModelForm):
    class Meta:
        model = PlannedEntry
        fields = '__all__'
