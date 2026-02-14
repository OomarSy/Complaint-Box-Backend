from rest_framework import serializers
from .models import Complaint

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ['id', 'title', 'reason', 'custom_reason', 'description', 'status', 'created_at']
        read_only_fields = ['id', 'status', 'created_at']
    
    def validate(self, attrs):
        reason = attrs.get("reason")
        custom_reason = attrs.get("custom_reason")

        if reason == "other" and not custom_reason:
            raise serializers.ValidationError({
                "custom_reason": "يجب إدخال سبب مخصص عند اختيار (أخرى)."
            })

        if reason != "other":
            attrs["custom_reason"] = None

        return attrs