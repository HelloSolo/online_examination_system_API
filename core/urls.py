from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('questions', views.QuestionViewset)
router.register('options', views.OptionViewset)
router.register('candidates', views.CandidateViewset)
router.register('respones', views.ResponseViewset)
router.register('scores', views.ScoreViewset)

urlpatterns = router.urls
