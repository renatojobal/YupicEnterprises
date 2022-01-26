# Django
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

# Rest framewkor imports
# ...

# Local project imports
from core.router import router
from core import views


# Other impoprts
# ...


urlpatterns = [

    # Rutas correspondientes a todos los modelos en general
    path('', include(router.urls)),


]