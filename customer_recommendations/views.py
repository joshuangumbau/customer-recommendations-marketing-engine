from rest_framework import viewsets
from rest_framework.response import Response
from .models import Customer, Recommendation
from .serializers import CustomerSerializer, RecommendationSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer