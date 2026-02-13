from rest_framework import serializers
from .models import Complaint

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ['id', 'title', 'reason', 'description', 'extra_data', 'status', 'created_at']
        read_only_fields = ['id', 'status', 'created_at']
