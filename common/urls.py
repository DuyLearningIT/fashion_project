from .views import ImageUploadView
from django.urls import path

urlpatterns = [
    path('upload-image/', ImageUploadView.as_view(), name='upload-image'),
]
