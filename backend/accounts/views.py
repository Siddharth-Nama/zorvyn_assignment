from rest_framework import generics
from .serializers import UserSerializer
from .permissions import IsAuthenticatedAndActive

class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedAndActive]

    def get_object(self):
        return self.request.user
