from rest_framework import serializers
from .models import kpiConfiguration
class kpiConfigurationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = kpiConfiguration
        fields = '__all__'