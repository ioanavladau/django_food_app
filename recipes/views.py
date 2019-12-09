from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RecipeSerializer
from .models import RecipeData

# Create your views here.

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = RecipeData.objects.all()
    serializer_class = RecipeSerializer


# create view for lunch
class LunchViewSet(viewsets.ModelViewSet):
    queryset = RecipeData.objects.filter(typ='lunch')
    serializer_class = RecipeSerializer


# create view for breakfast
class BreakfastViewSet(viewsets.ModelViewSet):
    queryset = RecipeData.objects.filter(typ='breakfast')
    serializer_class = RecipeSerializer

