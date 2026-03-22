from rest_framework import serializers
from .models import MedicalCard, ChecklistItem, Category

class ChecklistItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChecklistItem
        fields = ['id', 'task', 'order']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class MedicalCardSerializer(serializers.ModelSerializer):
    items = ChecklistItemSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = MedicalCard
        fields = ['id', 'title', 'description', 'image_url', 'category', 'items', 'created_at']
