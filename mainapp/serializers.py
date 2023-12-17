from rest_framework import serializers
from .models import *


class productSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class dataSerializers(serializers.ModelSerializer):
    class Meta:
        model = data
        fields = '__all__'