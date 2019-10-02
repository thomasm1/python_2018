from .api import ListViewSet, CardViewSet, ProjectViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'lists', ListViewSet)
router.register(r'cards', CardViewSet)
router.register(r'projects', ProjectViewSet, 'project')

urlpatterns = router.urls
