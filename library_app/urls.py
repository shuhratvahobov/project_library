from django.urls import path
from .views import LibrarySerializersView


urlpatterns = [
    

    path('api/v1/',LibrarySerializersView.as_view()),
]