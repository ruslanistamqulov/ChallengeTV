from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from users.views import logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
    path('',include('challenge.urls')),
    path('users/',include('django.contrib.auth.urls')),
    path('logout/', logout_view, name='logout')

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)