from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .settings import base
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="Pizza delivery API",
        default_version='v1',
        description="An api for contact list",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="vivekneosoft@gmail.com"),
        license=openapi.License(name="test License"),
    ),
    validators=['ssv', 'flex'],
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('simple.apps.core.urls',namespace='core')),
    path('', include('simple.apps.management.urls',namespace='management')),
    path('', include('simple.apps.others.urls',namespace='others')),
    path('', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
    path('^redoc', schema_view.with_ui('redoc', cache_timeout=None), name='schema-redoc'),
    path('auth/', include('djoser.urls.jwt')),
]

if base.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(base.MEDIA_URL,
                          document_root=base.MEDIA_ROOT)
    urlpatterns += static(base.STATIC_URL,
                          document_root=base.STATIC_ROOT)

