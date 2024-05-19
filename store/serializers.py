from rest_framework import serializers
from .models import *
from itertools import groupby

# Store detail serializer
class StoreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"