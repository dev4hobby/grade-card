from accounts.models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


user_viewset = UserViewSet.as_view({
    'get': 'get'
})