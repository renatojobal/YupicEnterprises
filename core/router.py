# Django imports

# Rest_framework imports
from rest_framework import routers

# Local imports
from core.views import ProjectViewset


# Other imports
# ...


router = routers.DefaultRouter()

router.register('projects', ProjectViewset)