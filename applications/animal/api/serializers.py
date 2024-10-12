from rest_framework import serializers
from applications.animal.models import Breed, Species, Animal, Status
from applications.treatment.api.serializers import TreatmentSerializer

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'

class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = '__all__'

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class AnimalSerializer(serializers.ModelSerializer):
    breed = BreedSerializer()
    species = SpeciesSerializer()
    status = StatusSerializer()
    treatments = TreatmentSerializer(many=True, read_only=True, source='treatment_set')

    class Meta:
        model = Animal
        fields = ["name","number","weight","file","image","breed", "species","status","treatments"]