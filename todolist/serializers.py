from rest_framework import serializers
from .models import todos

class todoSerializer(serializers.ModelSerializer):
    class Meta:
        model = todos
        fields = ('id', 'title', 'body',)