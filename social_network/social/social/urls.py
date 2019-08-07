from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('users/', include('users.urls')),
    # path('users/', include('django.contrib.auth.urls')),
    path('api/v1/social/', include('soc_net.urls')),
    # path('rest-auth/', include('rest_auth.urls')),
    path('api/v1/auth/', include('api.urls')),
    # path('api/v1/', include('likes.api.urls')),
    # path('', include(urls)),
]
