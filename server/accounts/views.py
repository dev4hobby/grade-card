from accounts.models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
    def update(self, request):
        serializer = UserSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


user_viewset = UserViewSet.as_view({
    'get': 'get',
    'post': 'update',
})