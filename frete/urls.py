
from django.contrib import admin
from django.urls import path, include
from api.views import create_city, delete_city
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create_city/', create_city, name='create_city'),
    path('delete_city/<int:pk>', delete_city, name='delete_city')
]
