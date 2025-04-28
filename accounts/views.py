from django.shortcuts import render, redirect
from django.http import JsonResponse

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from django.shortcuts import redirect
from allauth.account.views import PasswordResetFromKeyView


from .models import CustomUserModel, UserProfile
from .serializers import UserProfileSerializer, ProfileUpdateSerializer, UserSerializer

def email_confirmation(request, key):
    return redirect(f"http://localhost:3000/dj-rest-auth/registration/account-confirm-email/{key}")

def reset_password_confirm(request, uidb36, key):
    return PasswordResetFromKeyView.as_view()(request, uidb36=uidb36, key=key)

class UserProfileCreateView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#  for Profile Detail View
class UserProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile

# for update profile
class ProfileUpdateView(APIView):
    permission_classes = [IsAuthenticated] 

    def put(self, request):
        try:
            # Get the profile of the logged-in user
            profile = UserProfile.objects.get(user=request.user)
            serializer = ProfileUpdateSerializer(profile, data=request.data, partial=True)  
            
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Profile updated successfully!", "data": serializer.data}, status=status.HTTP_200_OK)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except UserProfile.DoesNotExist:
            return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions for the users.
    """
    queryset = CustomUserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CustomUserModel.objects.filter(id=self.request.user.id)