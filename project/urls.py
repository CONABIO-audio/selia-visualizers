from django.conf.urls import url
from django.conf.urls import include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static


urlpatterns = [
    url('admin/', admin.site.urls),
    url(
        r'^visualizers/',
        include(('selia_visualizers.urls', 'selia_visualizers'))),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
