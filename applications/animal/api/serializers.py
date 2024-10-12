from rest_framework import serializers
from applications.animal.models import Breed, Species, Animal, Status
from applications.treatment.models import Treatment
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
    breed = serializers.PrimaryKeyRelatedField(queryset=Breed.objects.all())
    species = serializers.PrimaryKeyRelatedField(queryset=Species.objects.all())
    status = serializers.PrimaryKeyRelatedField(queryset=Status.objects.all())
    treatment = serializers.PrimaryKeyRelatedField(many=True, queryset=Treatment.objects.all())
    class Meta:
        model = Animal
        fields = ["name","number","weight","file","image","breed", "species","status","treatment"]
    
    def to_representation(self, instance):
        """Modificar la representación para el GET."""
        # Llamamos al método original para obtener los datos serializados
        representation = super().to_representation(instance)
        # Reemplazamos los IDs de 'medicine' con los datos completos
        representation['breed'] = BreedSerializer(instance.breed).data
        representation['species'] = SpeciesSerializer(instance.species).data
        representation['status'] = StatusSerializer(instance.status).data
        representation['treatment'] = TreatmentSerializer(instance.treatment.all(), many=True).data
        return representation