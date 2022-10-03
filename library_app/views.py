from django.shortcuts import render
from django.views.generic import TemplateView
from .serializers import LibrarySerializers
from rest_framework.generics import ListCreateAPIView
from .models import Library
from rest_framework.filters import SearchFilter


class LibrarySerializersView(ListCreateAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializers
    filter_backends = [SearchFilter]
    search_fields = ['ISBN','title','author','first_publishing_year','number_of_pages','status']