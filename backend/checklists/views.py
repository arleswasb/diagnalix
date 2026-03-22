from rest_framework import generics

from .models import MedicalCard
from .serializers import MedicalCardSerializer


class MedicalCardList(generics.ListAPIView):
	queryset = MedicalCard.objects.all()
	serializer_class = MedicalCardSerializer
