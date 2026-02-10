from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def get_permissions(self):
    #     if self.action == "destroy":
    #         permission_classes = [IsAdminUser]
