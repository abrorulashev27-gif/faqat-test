from .models import Phone
from rest_framework import serializers

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'




