from django.contrib import admin
from django.urls import path, include
from pagina import views  # Asegúrate de importar las vistas adecuadamente
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pagina/', include('pagina.urls')),  # Incluye las URLs de tu aplicación 'pagina'
    path('browniesadd', views.browniesadd, name='browniesadd'),
    path('brownies/editar/<int:pk>', views.editar_brownie, name='editar_brownie'),
    path('brownies/eliminar/<int:pk>', views.eliminar_brownie, name='eliminar_brownie'),
    path('browniesUpdate', views.browniesUpdate, name='browniesUpdate'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
