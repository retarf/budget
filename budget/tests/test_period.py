import pytest
import datetime
from budget.tests import PeriodFactory


@pytest.fixture()
def period():
    name = datetime.datetime(year=2021, month=7, day=1)
    period = PeriodFactory(name=name)
    period.save()
    return period


@pytest.mark.django_db
class TestPeriodView:
    def test_list_view(self, client, period):
        response = client.get('/budget/period/')
        assert response.status_code == 200
        assert str(response.context['period_list'][0]) == "2021-07"

    def test_detail_view(self, client, period):
        url = f'/budget/period/{period.id}/'
        response = client.get(url)
        assert response.status_code == 200

    def test_create_view(self, client, period):
        response = client.get('/budget/period/create/')
        assert response.status_code == 200
