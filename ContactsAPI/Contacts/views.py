from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ContactSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Contact
# Create your views here.

class ContactList(ListCreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,) 

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)   

class ContactDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer 
    permission_classes = (IsAuthenticated,)
    lookup_field='id'

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)
