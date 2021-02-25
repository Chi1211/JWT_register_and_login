from django.urls import path 
from .views import NoteView
from rest_framework.routers import SimpleRouter

router=SimpleRouter()
router.register('notes', NoteView, basename="notes")
urlpatterns=router.urls
