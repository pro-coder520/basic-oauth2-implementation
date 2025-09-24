from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

def signin(request):
    return render(request, 'accounts/signin.html')

@api_view(['GET'])
def get_jwt_token(request):
    if request.user.is_authenticated:
        refresh = RefreshToken.for_user(request.user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    else:
        return Response({'error': 'User not authenticated'}, status=401)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def expenses(request):
    data = {
        'message': 'Welcome to the home page!',
        'user': request.user.email if request.user.is_authenticated else 'Guest'
    }
    return Response(data)