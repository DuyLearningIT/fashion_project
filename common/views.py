import cloudinary.uploader
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UploadImageSerializer


class ImageUploadView(APIView):
    def post(self, request):
        image = request.FILES.get("image")

        if not image:
            return Response({"error": "No image uploaded"}, status=400)

        result = cloudinary.uploader.upload(image)

        return Response(
            {
                "url": result["secure_url"],
                "public_id": result["public_id"],
            },
            status=status.HTTP_201_CREATED,
        )
