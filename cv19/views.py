from django.shortcuts import render
from .models import Corona
from rest_framework import viewsets
from rest_framework import permissions, authentication
from .serializers import CoronaSerializer


class CoronaViewSet(viewsets.ModelViewSet):
    queryset = Corona.objects.all()
    serializer_class = CoronaSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    
    # def get_queryset(self):
    #     user = self.request.user
    #     return List.objects.filter(owner=user)