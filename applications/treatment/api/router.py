from rest_framework.routers import DefaultRouter
from applications.treatment.api.views import *

router_treatment = DefaultRouter()
router_treatment.register(
    prefix='treatments', basename='treatments', viewset=TreatmentViewSet
)

router_treatment.register(
    prefix='medicines', basename='medicines', viewset=MedicineViewSet
)