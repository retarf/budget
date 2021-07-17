from django import forms

from budget.models import Period


class PeriodForm(forms.ModelForm):
    name = forms.DateField()
    class Meta:
        model = Period
