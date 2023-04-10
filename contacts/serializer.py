from rest_framework import fields, serializers
from .models import transportation, reviews, Contact


class TrasportationSerializer(serializers.ModelSerializer):
    class Meta :
        model = transportation
        fields = "__all__" 

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta :
        model = reviews
        fields = "__all__" 


class ContactSerializer(serializers.ModelSerializer):
    class Meta :
        model = Contact
        fields = "__all__" 
