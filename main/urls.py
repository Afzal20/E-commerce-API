from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import ProfileUpdateView, UserProfileCreateView, UserProfileDetailView, email_confirmation, reset_password_confirm
from catalg.views import index, serve_media
from .views import csrf_token_view, MyView
from allauth.account.views import PasswordResetFromKeyView, PasswordResetFromKeyDoneView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin-side-of-bindubritto/', admin.site.urls),
    path('api/', include("catalg.urls")),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path("password/reset/key/<uidb36>/<key>/", PasswordResetFromKeyView.as_view(), name="account_reset_password_from_key"),
    path("password/reset/key/done/",PasswordResetFromKeyDoneView.as_view(),name="account_reset_password_from_key_done",),
    path('profile/create/', UserProfileCreateView.as_view(), name='profile-create'),
    path('profile/', UserProfileDetailView.as_view(), name='profile-detail'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile-update'),
    # re_path(r'^.*$', TemplateView.as_view(template_name='index.html'), name='home'),
    path('api/csrf_token/', csrf_token_view, name='csrf_token'),
    path('api/myview/', MyView.as_view(), name='my_view'),
    re_path(r'^media/(?P<path>.*)$', serve_media, name='serve_media'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('', index, name='index'),

]



if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)