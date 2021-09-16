from rest_framework.response import Response
from .serializer import *
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.permissions import AllowAny


class LoginViewSet(ModelViewSet, TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class RegistrationViewSet(ModelViewSet, TokenObtainPairView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        return Response({
            "user": serializer.data,
            "refresh": res["refresh"],
            "token": res["access"],
            "status": "201"
        })

# class RegisterView(APIView):

#     def post(self, request):
#         try:
#             serializer = UserSerializer(data = request.data)
#             if not serializer.is_valid():
#                 return Response({
#                     'status':403,
#                     'errors': serializer.errors,
#                 })
#             serializer.save()

#             return Response({
#                 'status': 200, 'message':'an OTP sent to your number and email'
#             })
#         except Exception as e:
#             print(e)
#             return Response({
#                 'status':404,
#                 'error':'something went wrong'
#             })


# from rest_framework.views import APIView
# from .serializer import UserSerializer
# from rest_framework.response import Response
# from django.contrib.auth.models import User
# # from rest_framework.authentication import TokenAuthentication
# from rest_framework_simplejwt.tokens import RefreshToken

# class RegisterUser(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data = request.data)

#         if not serializer.is_valid():
#             print(serializer.errors)
#             return Response({'status': 403, 'errors':serializer.errors, 'message': 'Something Went Wrong'})

#         serializer.save()

#         user = User.objects.get(email = serializer.data['email'])
#         refresh = RefreshToken.for_user(user)

#         return ({
#         'status':200,
#         'payload':serializer.data,
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#         'message': 'your data is saved'
#     })