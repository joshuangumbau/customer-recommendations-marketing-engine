from rest_framework import serializers
from .models import Customer, Recommendations

class customerSerializer(serializers.ModelSerializer):
    class meta:
        model = Customer
        field = '__all__'
        
class RecommendationsSerializer(serializers.ModelSerializer):
    class meta:
        model = Recommendations
        field = '__all__'
        