from django.db import models
from django.urls import reverse


class Period(models.Model):
    name = models.DateField()

    def __str__(self):
        return self.name.strftime("%Y-%m")

    def get_absolute_url(self):
        return reverse('period-detail', kwargs={'pk': self.pk})


class BaseEntry(models.Model):
    period = models.ForeignKey('Period', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=120)
    value = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        abstract = True


class PlannedEntry(BaseEntry):
    repetitive = models.BooleanField()
    repeat_month = models.DateField()

    class Meta:
        abstract = True


class PlannedIncome(PlannedEntry):
    pass


class PlannedExpense(PlannedEntry):
    pass
