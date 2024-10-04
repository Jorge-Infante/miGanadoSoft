from rest_framework.routers import DefaultRouter
from applications.animal.api.views import *

router_animal = DefaultRouter()
router_animal.register(
    prefix='animals', basename='animals', viewset=AnimalViewset
)

router_animal.register(
    prefix='breeds', basename='breeds', viewset=BreedViewSet
)

router_animal.register(
    prefix='species', basename='species', viewset=SpeciesViewSet
)

router_animal.register(
    prefix='status', basename='status', viewset=StatusViewSet
)