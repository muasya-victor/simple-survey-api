from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet, ResponseViewSet

# Create a router and register our viewsets
router = DefaultRouter()
router.register(r'questions', QuestionViewSet, basename='question')
router.register(r'responses', ResponseViewSet, basename='response')

# Include the router URLs
urlpatterns = router.urls
