from django import forms

from budget.models import Period, Entry


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = '__all__'


class PeriodForm(forms.ModelForm):
    class Meta:
        model = Period
        fields = ["name"]
