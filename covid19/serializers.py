from rest_framework import serializers
from .models import Covid19

class covid19Serializer(serializers.ModelSerializer):
    class Meta:
        model = Covid19
        fields = "__all__"


