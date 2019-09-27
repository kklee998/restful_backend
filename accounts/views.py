from rest_framework import generics, permissions
from rest_framework.response import Response
from accounts.serializers import RegisterSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# Register new user
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_token_for_user(user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "refresh": token['refresh'],
            "access": token['access']
            })
    def get_token_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            }  
