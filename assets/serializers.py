from rest_framework import serializers 
from .models import Asset, Port, Application, WebMetadata,ScanResult

class PortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Port
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

class WebMetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebMetadata
        fields = '__all__'

class AssetSerializer(serializers.ModelSerializer):
    ports = PortSerializer(many=True, read_only=True)
    web_metadata = WebMetadataSerializer(read_only=True)

    class Meta:
        model = Asset
        fields = '__all__'




class ScanResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScanResult
        fields = '__all__'


