from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from accounts.views import GoogleLogin, ProfileUpdateView, UserProfileCreateView, UserProfileDetailView, email_confirmation, reset_password_confirm


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("catalg.urls")),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('reset/password/confirm/<int:uid>/<str:token>', reset_password_confirm, name="password_reset_confirm"),
    path('dj-rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('profile/create/', UserProfileCreateView.as_view(), name='profile-create'),
    path('profile/', UserProfileDetailView.as_view(), name='profile-detail'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile-update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
