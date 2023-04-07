from rest_framework import fields, serializers
from .models import Listing
from realtors.models import Realtor
from realtors.serializer import Realtorserializer


class listingserializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = "__all__"
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['realtor'] = Realtorserializer(instance.realtor).data
        return response