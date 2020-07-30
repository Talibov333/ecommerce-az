from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

# admin panel
admin.site.site_header = 'MoOnLight_StoRe'
admin.site.site_title = "MoOnLigHT"
admin.site.index_title = "Have a good Day :)"




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    # path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
