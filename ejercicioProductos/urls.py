from django.contrib import admin
from django.urls import path
from templatesApp.views import renderTemplate
from templatesApp.views import electronica
from templatesApp.views import juguetes
from templatesApp.views import ropa


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', renderTemplate),
    path('electronica/', electronica),
    path('juguetes/', juguetes),
    path('ropa/', ropa)

]
