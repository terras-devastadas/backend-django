from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

from customUser.views import CustomUserViewset, LogoutView
from exampleItem.views import ItemViewset

router = routers.DefaultRouter()
router.register(r"items", ItemViewset)
router.register(r"users", CustomUserViewset)

urlpatterns = [
    path("", include(router.urls)),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

