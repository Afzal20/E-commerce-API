from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import ProfileUpdateView, UserProfileCreateView, UserProfileDetailView, email_confirmation, reset_password_confirm
from .views import csrf_token_view, MyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("catalg.urls")),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('reset/password/confirm/<int:uid>/<str:token>', reset_password_confirm, name="password_reset_confirm"),
    path('profile/create/', UserProfileCreateView.as_view(), name='profile-create'),
    path('profile/', UserProfileDetailView.as_view(), name='profile-detail'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile-update'),
    # re_path(r'^.*$', TemplateView.as_view(template_name='index.html'), name='home'),
    path('api/csrf_token/', csrf_token_view, name='csrf_token'),
    path('api/myview/', MyView.as_view(), name='my_view'),
]

if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)