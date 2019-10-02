from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register('question', QuestionAPI)


urlpatterns = [
    path('', index, name='index'),
    path('', include(router.urls)),
    path('latest', latest, name='latest')
]