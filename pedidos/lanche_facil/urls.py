from django.contrib import admin
from django.urls import path
from pedidos.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
]