from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API - E-commerce",
      default_version='v1',
      description="API do e-commerce",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="gustavoguerra.gr@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


app_name = 'ecommerce'

urlpatterns = [
    path('admin/', admin.site.urls),
    url(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'
    ),
    url(
        r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    url(
        r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
    path('api/accounts/', include('ecommerce.accounts.urls'), name='accounts'),
    path('api/', include('ecommerce.product.urls'), name='product'),
    path(
        'api/auth/',
        include('oauth2_provider.urls', namespace='oauth2_provider')
    ),
]
