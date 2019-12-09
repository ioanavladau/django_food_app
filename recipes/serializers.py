from rest_framework import serializers
from .models import RecipeData

class RecipeSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = RecipeData
        fields = ['id', 'name', 'duration', 'rating', 'typ', 'image']