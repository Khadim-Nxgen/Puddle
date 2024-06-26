
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from core.views import privacy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
    path('items/',include('item.urls')),
    path('inbox/',include('conversation.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('privacy/',privacy, name="privacy"),
 ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
