from django.shortcuts import render
from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Realtor
from .serializer import Realtorserializer
# Create your views here.

class realtorapi(APIView):
    def get_object(self, pk):
        try:
            return Realtor.objects.get(pk=pk)
        except Realtor.DoesNotExist:
                raise Http404
        # get the employee by id otherwise all the employee
    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = Realtorserializer(data)
            return Response(serializer.data)

        else:
            data = Realtor.objects.filter(is_mvp=True)
            serializer = Realtorserializer(data, many=True)
            return Response(serializer.data)
      