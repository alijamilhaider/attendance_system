from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path("", include("apps.user.urls")),
                  path("", include("apps.attendance.urls")),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
