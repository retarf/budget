from rest_framework import routers
from budget import api


router = routers.DefaultRouter()
router.register(r"periods", api.PeriodViewSet, basename='period')
router.register(r"entries", api.EntryViewSet, basename='entry')
urlpatterns = router.urls