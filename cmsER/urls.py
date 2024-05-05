from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from realestatepro import views as realestatepro_views

urlpatterns = [
    path('', realestatepro_views.home, name='home'), # Mapeia a view home para a URL raiz
    path('admin/', admin.site.urls),
    path('realestatepro/', include('realestatepro.urls')),
    path('logout/', auth_views.LogoutView.as_view(template_name='admin/registration/logged_out.html'), name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # serve ficheiros estáticos através do Django em ambiente de desenvolvimento

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)