from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework.exceptions import ValidationError
from accounts.models import CustomUserModel, UserProfile
from django.utils.translation import gettext as _
from allauth.account.models import EmailAddress
from rest_framework import serializers

class CustomEmailAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailAddress
        fields = '__all__'

    def create(self, validated_data):
        validated_data['primary'] = True
        validated_data['verified'] = True
        return super().create(validated_data)


# class CustomRegisterSerializer(RegisterSerializer):
#     def validate_email(self, email):
#         if CustomUserModel.objects.filter(email=email).exists():
#             raise ValidationError(_("A user with this email already exists"))
#         return email


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__' 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ['id', 'email', 'first_name', 'last_name', 'is_active', 'date_joined', 'last_login', 'verified']


from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

class CustomRegisterSerializer(RegisterSerializer):
    username = None  # ← this tells the serializer to ignore username

    def validate_email(self, email):
        if CustomUserModel.objects.filter(email=email).exists():
            raise serializers.ValidationError("A user with this email already exists")
        return email

    def get_cleaned_data(self):
        return {
            'email': self.validated_data.get('email', ''),
            'password1': self.validated_data.get('password1', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
        }
