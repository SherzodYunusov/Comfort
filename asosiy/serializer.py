from rest_framework import serializers
from .models import *

class MahsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = '__all__'

class Qarzdorlik_sotuvchiSerializer(serializers.Serializer):
    class Meta:
        model = Qarzdorlik_sotuvchi
        fields = '__all__'

class Qarzdorlik_mijozSerializer(serializers.Serializer):
    class Meta:
        models = Qarzdorlik_mijoz
        fields = '__all__'

class KirimSerializer(serializers.Serializer):
    class Meta:
        models = Kirim
        fields = '__all__'

class FoydalanuvchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foydalanuvchi
        fields = '__all__'
