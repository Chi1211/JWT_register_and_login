from django.shortcuts import render
from rest_framework import viewsets
from .models import Notes
from .serializer import NotesSerializer
from rest_framework import permissions
# Create your views here.
class NoteView(viewsets.ModelViewSet): 
    queryset=Notes.objects.all()
    serializer_class=NotesSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)