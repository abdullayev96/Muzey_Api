from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/leader/', include("leader.urls")),
    path('api/connect/', include("connect.urls")),
    path('api/about/', include("about.urls")),
    path('api/gallery/', include("gallery.urls")),
    path('api/contact/', include("contact.urls")),
    path('api/new/', include("news.urls")),
    path('api/cat/', include("category.urls")),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#

#]
