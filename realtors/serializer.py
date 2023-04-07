from rest_framework import fields, serializers
from realtors.models import Realtor


class Realtorserializer(serializers.ModelSerializer):
    class Meta:
        model = Realtor
        fields = "__all__"