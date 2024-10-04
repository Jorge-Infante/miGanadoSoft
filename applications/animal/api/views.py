from rest_framework.viewsets import ModelViewSet
from applications.animal.models import Breed, Species, Animal, Status
from applications.animal.api.serializers import BreedSerializer, SpeciesSerializer, AnimalSerializer, StatusSerializer

class BreedViewSet(ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

class SpeciesViewSet(ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer

class StatusViewSet(ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class AnimalViewset(ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer