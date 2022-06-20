from django.urls import include, path
from rest_framework import routers

from students.viewset.student_viewset import StudentViewSet

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet, basename='students')
urlpatterns = [
    path('', include(router.urls)),
]
