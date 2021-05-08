from rest_framework import viewsets

from .models import ComprasItem
from .serializers import ComprasItemSerializer
class ComprasItemViewSet(viewsets.ModelViewSet):

    serializer_class = ComprasItemSerializer
    queryset = ComprasItem.objects.all()