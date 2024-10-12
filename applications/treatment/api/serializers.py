from rest_framework import serializers
from applications.treatment.models import Medicine, Treatment

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'

class TreatmentSerializer(serializers.ModelSerializer):
    medicine = serializers.PrimaryKeyRelatedField(many=True, queryset=Medicine.objects.all())
    class Meta:
        model = Treatment
        fields = ['id','name','medicine']
    
    def to_representation(self, instance):
        """Modificar la representación para el GET."""
        # Llamamos al método original para obtener los datos serializados
        representation = super().to_representation(instance)
        # Reemplazamos los IDs de 'medicine' con los datos completos
        representation['medicine'] = MedicineSerializer(instance.medicine.all(), many=True).data
        return representation
