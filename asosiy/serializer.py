from rest_framework import serializers
from .models import *

class MahsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = '__all__'

class Qarzdorlik_sotuvchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qarzdorlik_sotuvchi
        fields = '__all__'

class Qarzdorlik_mijozSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qarzdorlik_mijoz
        fields = '__all__'

class KirimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kirim
        fields = '__all__'

class FoydalanuvchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foydalanuvchi
        fields = '__all__'
