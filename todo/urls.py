from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from todo import views

router = DefaultRouter()
router.register(r'todo', views.TodoViewSet, basename='todo')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls))
]
