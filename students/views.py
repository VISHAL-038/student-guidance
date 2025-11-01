from rest_framework import generics, permissions
from .models import StudentProfile
from .serializers import StudentProfileSerializer

class StudentProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = StudentProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.studentprofile
