from django.contrib import admin
from django.urls import path, include
from django.utils.translation import gettext_lazy as _
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/', include('dj_rest_auth.urls')),
    path('api/v1/registration/', include('dj_rest_auth.registration.urls')),
    path("", include("common.urls", namespace="common")),
    path("profile/", include("users.urls", namespace="users")),

]

admin.site.site_header = _("Oddmentors Backend")
admin.site.site_title = _("Oddmentors Backend")
admin.site.index_title = _("Oddmentors Backend")

if settings.DEBUG:
    urlpatterns = urlpatterns + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns = urlpatterns + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )