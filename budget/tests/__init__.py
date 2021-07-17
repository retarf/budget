import factory

from budget.models import Period


class PeriodFactory(factory.Factory):

    class Meta:
        model = Period
