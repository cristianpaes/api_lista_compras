from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from compras.views import ComprasItemViewSet

router = routers.DefaultRouter()
router.register(
    'compras-item', ComprasItemViewSet,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
