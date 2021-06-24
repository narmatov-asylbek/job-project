from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import decorators
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.contrib.auth import get_user_model

from .serializers import UserSerializer, UserCreateSerializer

User = get_user_model()


@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def registration(request):
    serializer = UserCreateSerializer(data=request.data)
    if not serializer.is_valid(raise_exception=True):
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    else:
        user = serializer.save()
        print(user)
        res = {
            "status": True,
            "message": "Successfully registered",
        }
        return Response(res, status.HTTP_201_CREATED)


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()