import re
from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator


PERIOD_RE = r"\d{4}-[0-1]\d"


period_validator = RegexValidator(regex=re.compile(PERIOD_RE))


MONTHS = (
    ('01', '01'),
    ('02', '02'),
    ('03', '03'),
    ('04', '04'),
    ('05', '05'),
    ('06', '06'),
    ('07', '07'),
    ('08', '08'),
    ('09', '09'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
)


class Period(models.Model):
    name = models.CharField(max_length=7, unique=True, validators=[period_validator])

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('period-detail', kwargs={'pk': self.pk})


class BaseEntry(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    value = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        abstract = True


class Entry(BaseEntry):
    INCOME = 'in'
    EXPENSE = 'ex'
    CHOICES = [
        (INCOME, "income"),
        (EXPENSE, "expense"),
    ]
    description = models.CharField(max_length=120)
    period = models.ForeignKey('Period', on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=CHOICES, default=EXPENSE)
    repetitive = models.BooleanField()
    repeat_month = models.CharField(max_length=2, choices=MONTHS, default=MONTHS[0][0])


class Flow(BaseEntry):
    entry = models.ForeignKey('Entry', on_delete=models.CASCADE)
