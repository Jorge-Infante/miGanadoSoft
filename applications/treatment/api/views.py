from rest_framework.viewsets import ModelViewSet
from applications.treatment.models import Treatment, Medicine
from applications.treatment.api.serializers import TreatmentSerializer, MedicineSerializer

class TreatmentViewSet(ModelViewSet):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer

class MedicineViewSet(ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer