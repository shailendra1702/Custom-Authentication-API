from rest_framework.routers import DefaultRouter
from .views import *

routes = DefaultRouter(trailing_slash=False)

routes.register('users',UserViewSet,basename='users')

urlpatterns = [
    *routes.urls
]