from rest_framework.routers import DefaultRouter
from .views import *

routes = DefaultRouter(trailing_slash=False)

routes.register('auth/login',LoginViewSet,basename='auth-login')
routes.register('auth/register',RegistrationViewSet,basename='auth-register')
routes.register('auth/email-verify',VerifyEmail,basename='email-verify')
urlpatterns = [
    *routes.urls
]