from rest_framework import serializers
from .models import Counter,Shurt

class CounterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Counter
        fields = '__all__'

class ShurtSerializer(serializers.ModelSerializer):
    code = serializers.CharField(read_only=True)

    class Meta:
        model = Shurt
        fields = '__all__'